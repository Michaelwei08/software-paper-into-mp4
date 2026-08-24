# Paper to MP3

Fetch an AI research paper, summarize each extracted paragraph in Simplified Chinese, and export:

- a Markdown text summary
- an MP3 narration of the Chinese summaries
- optionally, a silent MP4 slide deck containing the Chinese summaries

The default workflow is free: it uses a local Ollama model for summarization, not a paid API. The current implementation accepts either a paper URL or a recent arXiv AI/ML discovery mode. arXiv `abs` URLs, arXiv `pdf` URLs, and direct PDF URLs work best.

## Setup

Install Ollama, then pull a Chinese-capable local model:

```powershell
ollama pull qwen2.5:7b-instruct
```

Then install this project:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

MP3 narration uses `edge-tts`, which is free and does not require an API key. MP4 generation remains available with `--output-format mp4` or `--output-format both`.

## Usage

Summarize a specific paper:

```powershell
paper-to-mp4 --url "https://arxiv.org/abs/2405.21060"
```

Find a recent AI/ML paper from arXiv and summarize it:

```powershell
paper-to-mp4 --latest-ai
```

Limit cost and video length:

By default, the command summarizes all extracted body paragraphs before `References` or `Bibliography`.

Limit runtime while testing:

```powershell
paper-to-mp4 --url "https://arxiv.org/abs/2405.21060" --max-paragraphs 5
```

Generate both MP3 and MP4:

```powershell
paper-to-mp4 --url "https://arxiv.org/abs/2405.21060" --output-format both
```

Use a smaller local model if your computer is slow or has limited memory:

```powershell
ollama pull qwen2.5:3b
paper-to-mp4 --url "https://arxiv.org/abs/2405.21060" --model qwen2.5:3b
```

Optional paid OpenAI backend:

```powershell
python -m pip install -e ".[openai]"
$env:OPENAI_API_KEY = "your-api-key"
paper-to-mp4 --url "https://arxiv.org/abs/2405.21060" --summarizer openai --model gpt-4.1-mini
```

Outputs are written to `outputs/`:

```text
outputs/<paper-title>.zh-summary.md
outputs/<paper-title>.zh-summary.mp3
```

## Notes

- Ollama must be installed and running for the free local workflow.
- `--latest-ai` uses the arXiv API sorted by newest submissions, then applies a simple title/abstract keyword heuristic to select one candidate.
- The CLI skips references by default. Pass `--include-references` to include them.
- Official Ollama references: Windows install docs at <https://docs.ollama.com/windows>, API docs at <https://docs.ollama.com/api/generate>, and Qwen2.5 model page at <https://ollama.com/library/qwen2.5>.
