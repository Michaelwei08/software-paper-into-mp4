from __future__ import annotations

import html
import urllib.parse
import xml.etree.ElementTree as ET

import requests

from .models import Paper
from .text import normalize_space

ARXIV_API = "https://export.arxiv.org/api/query"
AI_QUERY = "(cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:stat.ML)"
IMPORTANT_TERMS = (
    "agent",
    "reasoning",
    "multimodal",
    "language model",
    "llm",
    "diffusion",
    "alignment",
    "robot",
    "benchmark",
    "vision-language",
    "reinforcement learning",
)


def find_latest_ai_paper(*, max_results: int = 25, timeout: int = 30) -> Paper:
    params = {
        "search_query": AI_QUERY,
        "start": "0",
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    response = requests.get(ARXIV_API, params=params, timeout=timeout)
    response.raise_for_status()
    papers = _parse_feed(response.text)
    if not papers:
        raise RuntimeError("arXiv returned no AI papers for the configured query.")
    return max(papers, key=_importance_score)


def _parse_feed(feed_xml: str) -> list[Paper]:
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
    }
    root = ET.fromstring(feed_xml)
    papers: list[Paper] = []
    for entry in root.findall("atom:entry", ns):
        title = normalize_space(_text(entry, "atom:title", ns))
        abstract = normalize_space(_text(entry, "atom:summary", ns))
        url = _text(entry, "atom:id", ns)
        published = _text(entry, "atom:published", ns)
        authors = tuple(
            html.unescape(_text(author, "atom:name", ns))
            for author in entry.findall("atom:author", ns)
        )
        pdf_url = _pdf_link(entry, ns)
        papers.append(
            Paper(
                title=html.unescape(title),
                url=url,
                pdf_url=pdf_url,
                authors=authors,
                abstract=html.unescape(abstract),
                published=published,
                source="arxiv",
            )
        )
    return papers


def _pdf_link(entry: ET.Element, ns: dict[str, str]) -> str | None:
    for link in entry.findall("atom:link", ns):
        if link.attrib.get("title") == "pdf":
            return link.attrib.get("href")
    return None


def _text(element: ET.Element, path: str, ns: dict[str, str]) -> str:
    found = element.find(path, ns)
    return "" if found is None or found.text is None else found.text


def _importance_score(paper: Paper) -> int:
    text = f"{paper.title}\n{paper.abstract or ''}".lower()
    return sum(3 if term in paper.title.lower() else 1 for term in IMPORTANT_TERMS if term in text)


def arxiv_pdf_url(url: str) -> str | None:
    parsed = urllib.parse.urlparse(url)
    if "arxiv.org" not in parsed.netloc:
        return None
    paper_id = parsed.path.rsplit("/", 1)[-1]
    if not paper_id:
        return None
    if "/pdf/" in parsed.path:
        return url
    if "/abs/" in parsed.path:
        return f"https://arxiv.org/pdf/{paper_id}"
    return None
