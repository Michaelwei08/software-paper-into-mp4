from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Paper:
    title: str
    url: str
    pdf_url: str | None = None
    authors: tuple[str, ...] = ()
    abstract: str | None = None
    published: str | None = None
    source: str = "url"


@dataclass(frozen=True)
class ParagraphSummary:
    index: int
    original: str
    chinese_summary: str


@dataclass(frozen=True)
class RunResult:
    paper: Paper
    summaries: tuple[ParagraphSummary, ...]
