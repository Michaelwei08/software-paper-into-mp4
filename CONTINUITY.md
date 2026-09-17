# CONTINUITY.md

## Snapshot
- Goal: Create a Python project that fetches an AI paper from URL or recent arXiv discovery, summarizes each paragraph in Chinese, and exports text plus MP3.
- Now: 2026-04-29 [TOOL]: Full body workflow ran successfully on `https://arxiv.org/abs/2509.04664`.
- Next: 2026-04-29 [USER]: Review generated Markdown and MP3 in `outputs/`.
- Open questions: None.

## Invariants / Constraints
- 2026-04-29 [USER]: Workspace is `<WORKSPACE>/software_paper_into_mp4`.
- 2026-04-29 [USER]: Preserve small, safe, modular changes; avoid files over 300 lines of code.
- 2026-04-29 [USER]: No host system package installs unless explicitly instructed.

## Decisions
- D001 ACTIVE 2026-04-29 [ASSUMPTION]: Use a Python CLI package because the requested workflow is document processing plus media generation.
- D002 SUPERSEDED 2026-04-29 [ASSUMPTION]: Use OpenAI Responses API for high-quality paragraph-by-paragraph Chinese summaries; superseded by D004 because user wants free execution.
- D003 ACTIVE 2026-04-29 [CODE]: Generate a silent MP4 summary deck with rendered Chinese text slides; audio/TTS is out of initial scope.
- D004 ACTIVE 2026-04-29 [USER]: Use free local Ollama summarization by default; OpenAI remains optional only when explicitly selected.
- D005 ACTIVE 2026-04-29 [USER]: Generate MP3 narration instead of MP4 by default.

## State
### Done (recent)
- 2026-04-29 [TOOL]: Confirmed workspace has no visible project files.
- 2026-04-29 [TOOL]: Confirmed Python 3.13 is available; `ffmpeg` command is not installed.
- 2026-04-29 [CODE]: Added Python package with arXiv discovery, paper text extraction, OpenAI Chinese summarization, Markdown output, and silent MP4 rendering.
- 2026-04-29 [CODE]: Added README setup and usage instructions.
- 2026-04-29 [CODE]: Replaced paid OpenAI default with local Ollama backend using `qwen2.5:7b-instruct`; moved OpenAI package to optional dependency.
- 2026-04-29 [TOOL]: Ran user-requested `irm https://ollama.com/install.ps1 | iex`; installed Ollama 0.22.0.
- 2026-04-29 [TOOL]: Started Ollama server in the background; `curl.exe http://localhost:11434/api/version` returned `{"version":"0.22.0"}`.
- 2026-04-29 [TOOL]: Pulled Ollama model `qwen2.5:7b-instruct` (4.7 GB).
- 2026-04-29 [TOOL]: Ran `uv run paper-to-mp4 --url "https://arxiv.org/abs/2509.04664"` successfully.
- 2026-04-29 [TOOL]: Generated `outputs/input-paper.zh-summary.md` and `outputs/input-paper.zh-summary.mp4`.
- 2026-04-29 [CODE]: Changed default `--max-paragraphs` from 8 to unlimited, added default References/Bibliography cutoff, and added MP3 narration via `edge-tts`.
- 2026-04-29 [TOOL]: Re-ran `uv run paper-to-mp4 --url "https://arxiv.org/abs/2509.04664"`; summarized 35 body paragraphs and generated MP3.

### Now
- 2026-04-29 [TOOL]: Generated Markdown is 63,036 bytes and MP3 is 4,165,344 bytes.

### Next
- 2026-04-29 [USER]: Open `outputs/input-paper.zh-summary.md` and `outputs/input-paper.zh-summary.mp3`.

## Working set
- `CONTINUITY.md`
- `pyproject.toml`
- `README.md`
- `src/paper_to_mp4/`
- `uv.lock`
- `outputs/input-paper.zh-summary.md`
- `outputs/input-paper.zh-summary.mp3`
- `outputs/input-paper.zh-summary.mp4`

## Open questions
- 2026-04-29 [ASSUMPTION]: "latest important new paper" is implemented initially as latest arXiv AI/ML papers ranked by simple title/abstract keyword heuristic.

## Incidents
- Incident: PowerShell UTF-8 display warning
  Symptoms: Tool output includes `PropertySetterNotSupportedInConstrainedLanguage` and Chinese text appears mojibake in `Get-Content`.
  Evidence: 2026-04-29 [TOOL]: Python `unicode_escape` read confirmed Markdown contains valid Chinese Unicode text.
  Mitigation: Open the Markdown in an editor/browser or read with Python UTF-8.
  Status: ACTIVE.

## Receipts
- 2026-04-29 [TOOL]: `Get-Date -Format o` -> `2026-04-29T17:36:28.1131074-07:00`.
- 2026-04-29 [TOOL]: OpenAI official docs search -> Responses API uses `client.responses.create(...)`.
- 2026-04-29 [TOOL]: `python -m compileall src` -> passed.
- 2026-04-29 [TOOL]: `$env:PYTHONPATH='src'; python -m paper_to_mp4 --help` -> passed.
- 2026-04-29 [TOOL]: `git status --short` -> workspace is not a git repository.
- 2026-04-29 [WEB]: Official Ollama docs confirm local API base `http://localhost:11434/api` and non-streaming `/api/generate` with `stream: false`.
- 2026-04-29 [WEB]: Official Ollama Qwen2.5 page lists `qwen2.5:7b-instruct` and multilingual Chinese support.
- 2026-04-29 [TOOL]: `Get-Command ollama` -> no Ollama executable found in current PATH.
- 2026-04-29 [TOOL]: `irm https://ollama.com/install.ps1 | iex` -> install complete.
- 2026-04-29 [TOOL]: `& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" --version` -> `ollama version is 0.22.0`.
- 2026-04-29 [TOOL]: `curl.exe -sS http://localhost:11434/api/version` -> `{"version":"0.22.0"}`.
- 2026-04-29 [TOOL]: `& "<HOME>\AppData\Local\Programs\Ollama\ollama.exe" pull qwen2.5:7b-instruct` -> success.
- 2026-04-29 [TOOL]: `uv run paper-to-mp4 --url "https://arxiv.org/abs/2509.04664"` -> success; wrote Markdown and MP4.
- 2026-04-29 [TOOL]: `Get-ChildItem outputs` -> Markdown 14,539 bytes; MP4 461,010 bytes.
- 2026-04-29 [TOOL]: `python -m compileall src` -> passed after MP3 changes.
- 2026-04-29 [TOOL]: `$env:PYTHONPATH='src'; python -m paper_to_mp4 --help` -> passed after MP3 changes.
- 2026-04-29 [TOOL]: `uv run paper-to-mp4 --url "https://arxiv.org/abs/2509.04664"` -> success; `Paragraphs summarized: 35`, wrote Markdown and MP3.
- 2026-04-29 [TOOL]: `Get-ChildItem outputs` -> Markdown 63,036 bytes; MP3 4,165,344 bytes.
