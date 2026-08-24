from __future__ import annotations

import re
import tempfile
from html.parser import HTMLParser
from pathlib import Path

import requests
from pypdf import PdfReader

from .arxiv_client import arxiv_pdf_url
from .models import Paper
from .text import normalize_space


def paper_from_url(url: str, *, title: str | None = None) -> Paper:
    pdf_url = arxiv_pdf_url(url)
    return Paper(title=title or "Input paper", url=url, pdf_url=pdf_url, source="url")


def extract_paper_text(paper: Paper, *, cache_dir: Path, timeout: int = 60) -> str:
    cache_dir.mkdir(parents=True, exist_ok=True)
    source_url = paper.pdf_url or paper.url
    response = requests.get(source_url, timeout=timeout)
    response.raise_for_status()
    content_type = response.headers.get("content-type", "").lower()
    if source_url.lower().endswith(".pdf") or "application/pdf" in content_type:
        pdf_path = _write_temp_pdf(response.content, cache_dir)
        return extract_pdf_text(pdf_path)
    return _extract_html_text(response.text)


def extract_pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    page_texts = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        if page_text.strip():
            page_texts.append(page_text)
    text = "\n\n".join(page_texts)
    if not text.strip():
        raise RuntimeError(f"No extractable text found in PDF: {path}")
    return normalize_space(text)


def _write_temp_pdf(content: bytes, cache_dir: Path) -> Path:
    with tempfile.NamedTemporaryFile(dir=cache_dir, suffix=".pdf", delete=False) as handle:
        handle.write(content)
        return Path(handle.name)


def _extract_html_text(html_text: str) -> str:
    parser = _TextHTMLParser()
    parser.feed(html_text)
    text = parser.text()
    if not text:
        raise RuntimeError("No extractable text found in HTML page.")
    return text


class _TextHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []
        self._skip = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip = True
        if tag in {"p", "div", "section", "article", "br", "h1", "h2", "h3"}:
            self._parts.append("\n\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip = False
        if tag in {"p", "div", "section", "article"}:
            self._parts.append("\n\n")

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self._parts.append(data)

    def text(self) -> str:
        joined = "".join(self._parts)
        joined = re.sub(r"\n\s*\n\s*\n+", "\n\n", joined)
        return normalize_space(joined)
