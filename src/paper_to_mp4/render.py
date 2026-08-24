from __future__ import annotations

from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from .models import RunResult
from .text import compact_for_slide


WIDTH = 1280
HEIGHT = 720
BG = (249, 250, 252)
INK = (31, 35, 40)
MUTED = (89, 99, 110)
ACCENT = (22, 119, 255)


def render_summary_mp4(
    result: RunResult,
    path: Path,
    *,
    seconds_per_slide: float = 4.0,
    fps: int = 24,
    font_path: Path | None = None,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    title_font = _font(font_path, 44)
    body_font = _font(font_path, 34)
    meta_font = _font(font_path, 24)
    frames_per_slide = max(1, int(seconds_per_slide * fps))

    slides = [_title_slide(result, title_font, body_font, meta_font)]
    for item in result.summaries:
        slides.append(_summary_slide(item.index, len(result.summaries), item.chinese_summary, body_font, meta_font))

    with imageio.get_writer(
        path,
        fps=fps,
        codec="libx264",
        quality=8,
        macro_block_size=16,
    ) as writer:
        for slide in slides:
            frame = np.asarray(slide.convert("RGB"))
            for _ in range(frames_per_slide):
                writer.append_data(frame)


def _title_slide(result: RunResult, title_font: ImageFont.FreeTypeFont, body_font, meta_font) -> Image.Image:
    image = _base()
    draw = ImageDraw.Draw(image)
    draw.text((72, 64), "AI Paper Summary", font=meta_font, fill=ACCENT)
    _draw_wrapped(draw, result.paper.title, (72, 120), title_font, INK, max_width=1120, line_gap=14)
    meta = result.paper.published or result.paper.source
    authors = ", ".join(result.paper.authors[:4])
    if authors and len(result.paper.authors) > 4:
        authors += " et al."
    _draw_wrapped(draw, authors or meta, (72, 410), body_font, MUTED, max_width=1120, line_gap=10)
    _draw_footer(draw, 0, len(result.summaries), meta_font)
    return image


def _summary_slide(index: int, total: int, summary: str, body_font, meta_font) -> Image.Image:
    image = _base()
    draw = ImageDraw.Draw(image)
    draw.text((72, 60), f"Paragraph {index}", font=meta_font, fill=ACCENT)
    _draw_wrapped(
        draw,
        compact_for_slide(summary),
        (72, 132),
        body_font,
        INK,
        max_width=1120,
        line_gap=18,
    )
    _draw_footer(draw, index, total, meta_font)
    return image


def _base() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, WIDTH, 10), fill=ACCENT)
    return image


def _draw_footer(draw: ImageDraw.ImageDraw, index: int, total: int, font) -> None:
    label = "Title" if index == 0 else f"Summary slide {index}"
    draw.text((72, HEIGHT - 70), label, font=font, fill=MUTED)
    draw.text((WIDTH - 220, HEIGHT - 70), f"{index + 1}/{total + 1}", font=font, fill=MUTED)


def _draw_wrapped(draw: ImageDraw.ImageDraw, text: str, xy: tuple[int, int], font, fill, *, max_width: int, line_gap: int) -> None:
    x, y = xy
    for line in _wrap_by_pixels(draw, text, font, max_width):
        draw.text((x, y), line, font=font, fill=fill)
        bbox = draw.textbbox((x, y), line, font=font)
        y += bbox[3] - bbox[1] + line_gap


def _wrap_by_pixels(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.splitlines() or [text]:
        current = ""
        for char in paragraph:
            candidate = current + char
            if draw.textlength(candidate, font=font) <= max_width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = char
        if current:
            lines.append(current)
    return lines


def _font(font_path: Path | None, size: int) -> ImageFont.FreeTypeFont:
    candidates = []
    if font_path:
        candidates.append(font_path)
    candidates.extend(
        [
            Path("C:/Windows/Fonts/msyh.ttc"),
            Path("C:/Windows/Fonts/simhei.ttf"),
            Path("C:/Windows/Fonts/arial.ttf"),
        ]
    )
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default(size=size)
