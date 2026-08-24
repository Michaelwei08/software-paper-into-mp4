from __future__ import annotations

from pathlib import Path

from .models import RunResult


def write_markdown_summary(result: RunResult, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {result.paper.title}",
        "",
        f"- Source: {result.paper.url}",
    ]
    if result.paper.pdf_url:
        lines.append(f"- PDF: {result.paper.pdf_url}")
    if result.paper.published:
        lines.append(f"- Published: {result.paper.published}")
    if result.paper.authors:
        lines.append(f"- Authors: {', '.join(result.paper.authors)}")
    lines.extend(["", "## Paragraph Summaries", ""])

    for item in result.summaries:
        lines.extend(
            [
                f"### Paragraph {item.index}",
                "",
                "**中文总结**",
                "",
                item.chinese_summary,
                "",
                "<details>",
                "<summary>Original paragraph</summary>",
                "",
                item.original,
                "",
                "</details>",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")
