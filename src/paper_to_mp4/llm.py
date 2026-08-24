from __future__ import annotations

import json
import os
from collections.abc import Iterable

import requests

from .models import ParagraphSummary


DEFAULT_BACKEND = "ollama"
DEFAULT_OLLAMA_URL = "http://localhost:11434"
DEFAULT_OLLAMA_MODEL = "qwen2.5:7b-instruct"
DEFAULT_OPENAI_MODEL = "gpt-4.1-mini"


def summarize_paragraphs_zh(
    paragraphs: Iterable[str],
    *,
    backend: str = DEFAULT_BACKEND,
    model: str | None = None,
    max_output_tokens: int = 450,
) -> tuple[ParagraphSummary, ...]:
    if backend == "ollama":
        return _summarize_with_ollama(
            paragraphs,
            model=model or DEFAULT_OLLAMA_MODEL,
            max_output_tokens=max_output_tokens,
        )
    if backend == "openai":
        return _summarize_with_openai(
            paragraphs,
            model=model or DEFAULT_OPENAI_MODEL,
            max_output_tokens=max_output_tokens,
        )
    raise RuntimeError(f"Unknown summarizer backend: {backend}")


def _summarize_with_ollama(
    paragraphs: Iterable[str],
    *,
    model: str,
    max_output_tokens: int,
) -> tuple[ParagraphSummary, ...]:
    base_url = os.environ.get("OLLAMA_BASE_URL", DEFAULT_OLLAMA_URL).rstrip("/")
    results: list[ParagraphSummary] = []
    for index, paragraph in enumerate(paragraphs, start=1):
        summary = _summarize_one_ollama(
            base_url,
            paragraph,
            model=model,
            max_output_tokens=max_output_tokens,
        )
        results.append(ParagraphSummary(index=index, original=paragraph, chinese_summary=summary))
    return tuple(results)


def _summarize_with_openai(
    paragraphs: Iterable[str],
    *,
    model: str,
    max_output_tokens: int,
) -> tuple[ParagraphSummary, ...]:
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is required for Chinese summarization. "
            "Set it in the environment before running this command."
        )

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("Install the optional OpenAI package before using --summarizer openai.") from exc

    client = OpenAI()
    results: list[ParagraphSummary] = []
    for index, paragraph in enumerate(paragraphs, start=1):
        summary = _summarize_one_openai(client, paragraph, model=model, max_output_tokens=max_output_tokens)
        results.append(ParagraphSummary(index=index, original=paragraph, chinese_summary=summary))
    return tuple(results)


def _summarize_one_ollama(
    base_url: str,
    paragraph: str,
    *,
    model: str,
    max_output_tokens: int,
) -> str:
    payload = {
        "model": model,
        "system": (
            "You are a careful research paper summarizer. "
            "Return Simplified Chinese only inside valid JSON."
        ),
        "prompt": _prompt(paragraph),
        "format": "json",
        "stream": False,
        "options": {
            "num_predict": max_output_tokens,
            "temperature": 0.2,
        },
    }
    try:
        response = requests.post(f"{base_url}/api/generate", json=payload, timeout=180)
        response.raise_for_status()
    except requests.ConnectionError as exc:
        raise RuntimeError(
            "Could not connect to Ollama at "
            f"{base_url}. Install/start Ollama and run: ollama pull {model}"
        ) from exc
    except requests.HTTPError as exc:
        detail = exc.response.text[:500] if exc.response is not None else ""
        raise RuntimeError(
            f"Ollama request failed for model '{model}'. "
            f"Make sure it is installed with: ollama pull {model}. {detail}"
        ) from exc

    data = response.json()
    return _parse_summary_json(data.get("response", ""))


def _summarize_one_openai(
    client,
    paragraph: str,
    *,
    model: str,
    max_output_tokens: int,
) -> str:
    response = client.responses.create(
        model=model,
        instructions=(
            "You are a careful research paper summarizer. "
            "Do not invent details that are not supported by the paragraph."
        ),
        input=_prompt(paragraph),
        max_output_tokens=max_output_tokens,
    )
    return _parse_summary_json(response.output_text)


def _prompt(paragraph: str) -> str:
    return (
        "Summarize the following paper paragraph in Simplified Chinese. "
        "Keep the summary faithful, concrete, and 1-3 sentences. "
        'Return JSON only in this shape: {"summary_zh": "..."}.\n\n'
        f"Paragraph:\n{paragraph}"
    )


def _parse_summary_json(output_text: str) -> str:
    output_text = output_text.strip()
    try:
        data = json.loads(output_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Model did not return valid JSON: {output_text[:300]}") from exc
    summary = data.get("summary_zh")
    if not isinstance(summary, str) or not summary.strip():
        raise RuntimeError(f"Model JSON missing non-empty summary_zh: {output_text[:300]}")
    return summary.strip()
