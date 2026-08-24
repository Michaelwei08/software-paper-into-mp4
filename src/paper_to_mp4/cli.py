from __future__ import annotations

import argparse
import re
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    output_dir = args.output_dir.resolve()
    cache_dir = args.cache_dir.resolve()

    from .arxiv_client import find_latest_ai_paper
    from .audio import render_summary_mp3
    from .fetcher import extract_paper_text, paper_from_url
    from .llm import summarize_paragraphs_zh
    from .models import RunResult
    from .output import write_markdown_summary
    from .render import render_summary_mp4
    from .text import split_paragraphs, strip_references

    paper = find_latest_ai_paper(max_results=args.search_results) if args.latest_ai else paper_from_url(args.url)
    text = extract_paper_text(paper, cache_dir=cache_dir)
    if not args.include_references:
        text = strip_references(text)
    paragraphs = split_paragraphs(text, max_chars=args.max_paragraph_chars)
    if args.max_paragraphs is not None:
        paragraphs = paragraphs[: args.max_paragraphs]
    if not paragraphs:
        raise RuntimeError("No usable paragraphs were extracted from the paper.")

    summaries = summarize_paragraphs_zh(
        paragraphs,
        backend=args.summarizer,
        model=args.model,
        max_output_tokens=args.max_output_tokens,
    )
    result = RunResult(paper=paper, summaries=summaries)

    stem = _safe_stem(paper.title)
    markdown_path = output_dir / f"{stem}.zh-summary.md"
    write_markdown_summary(result, markdown_path)
    print(f"Paragraphs summarized: {len(summaries)}")
    print(f"Text summary: {markdown_path}")

    if args.output_format in {"mp3", "both"}:
        mp3_path = output_dir / f"{stem}.zh-summary.mp3"
        render_summary_mp3(result, mp3_path, voice=args.voice)
        print(f"MP3 summary:  {mp3_path}")

    if args.output_format in {"mp4", "both"}:
        mp4_path = output_dir / f"{stem}.zh-summary.mp4"
        render_summary_mp4(
            result,
            mp4_path,
            seconds_per_slide=args.seconds_per_slide,
            fps=args.fps,
            font_path=args.font,
        )
        print(f"MP4 summary:  {mp4_path}")
    return 0


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize an AI paper paragraph-by-paragraph in Chinese and render text/audio outputs."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--url", help="Paper URL. arXiv abs/pdf URLs and direct PDF URLs work best.")
    source.add_argument("--latest-ai", action="store_true", help="Find a recent AI/ML paper on arXiv.")

    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    parser.add_argument("--cache-dir", type=Path, default=Path(".cache/papers"))
    parser.add_argument(
        "--summarizer",
        choices=("ollama", "openai"),
        default="ollama",
        help="Summarization backend. Ollama is local and free.",
    )
    parser.add_argument("--model", default=None, help="Model name for the selected summarizer.")
    parser.add_argument("--max-paragraphs", type=int, default=None, help="Optional cap on extracted paragraphs.")
    parser.add_argument("--max-paragraph-chars", type=int, default=1800)
    parser.add_argument("--max-output-tokens", type=int, default=450)
    parser.add_argument("--search-results", type=int, default=25, help="Recent arXiv candidates to rank.")
    parser.add_argument("--include-references", action="store_true", help="Also summarize references/bibliography.")
    parser.add_argument("--output-format", choices=("mp3", "mp4", "both"), default="mp3")
    parser.add_argument("--voice", default="zh-CN-XiaoxiaoNeural", help="edge-tts voice for MP3 narration.")
    parser.add_argument("--seconds-per-slide", type=float, default=4.0)
    parser.add_argument("--fps", type=int, default=24)
    parser.add_argument("--font", type=Path, default=None, help="Optional .ttf/.ttc font path for Chinese text.")
    return parser.parse_args(argv)


def _safe_stem(title: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", title).strip("-").lower()
    return (stem or "paper")[:90]
