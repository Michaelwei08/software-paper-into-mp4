from __future__ import annotations

import asyncio
from pathlib import Path

import edge_tts

from .models import RunResult


DEFAULT_VOICE = "zh-CN-XiaoxiaoNeural"


def render_summary_mp3(
    result: RunResult,
    path: Path,
    *,
    voice: str = DEFAULT_VOICE,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = _audio_script(result)
    asyncio.run(_save_mp3(text, path, voice=voice))


async def _save_mp3(text: str, path: Path, *, voice: str) -> None:
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(str(path))


def _audio_script(result: RunResult) -> str:
    lines = [f"论文中文总结。标题：{result.paper.title}。"]
    for item in result.summaries:
        lines.append(f"第{item.index}段。{item.chinese_summary}")
    return "\n".join(lines)
