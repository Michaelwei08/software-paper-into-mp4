from __future__ import annotations

import re
import textwrap


def normalize_space(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_paragraphs(text: str, *, max_chars: int = 1800) -> list[str]:
    normalized = normalize_space(text)
    raw_parts = [part.strip() for part in re.split(r"\n\s*\n", normalized)]
    paragraphs: list[str] = []
    for part in raw_parts:
        if len(part) < 80:
            continue
        paragraphs.extend(_split_long_text(part, max_chars=max_chars))
    return paragraphs


def strip_references(text: str) -> str:
    match = re.search(r"(?im)^\s*(references|bibliography)\s*$", text)
    if not match:
        return text
    return text[: match.start()].strip()


def _split_long_text(text: str, *, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]

    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        candidate = f"{current} {sentence}".strip()
        if len(candidate) <= max_chars:
            current = candidate
            continue
        if current:
            chunks.append(current)
        if len(sentence) <= max_chars:
            current = sentence
        else:
            chunks.extend(textwrap.wrap(sentence, width=max_chars))
            current = ""
    if current:
        chunks.append(current)
    return chunks


def compact_for_slide(text: str, *, max_chars: int = 420) -> str:
    text = normalize_space(text).replace("\n", " ")
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "..."
