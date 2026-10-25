# CLAUDE.md

Claude Code loads this file and ignores `AGENTS.md`. The import below pulls in the
shared CrewAI guidance so every coding assistant works from the same instructions.
Keep shared conventions in `AGENTS.md`; add Claude-specific notes under the import.

@AGENTS.md

## Project specifics

JSON-first CrewAI project (no Python source yet; `tools/` is referenced by the README but doesn't exist). Python `>=3.10,<3.14`, managed with `uv`.

- Run: `crewai run` (prompts for any `{topic}` placeholder not set in `crew.jsonc` `inputs`). There is no test or lint setup.
- `crew.jsonc` defines a sequential two-task pipeline: `research_the_five_most_task` (researcher) → `using_the_research_brief_task` (writer, receives the first via `"context"`). Tasks reference agents by filename in `agents/<name>.jsonc`.
- The researcher file and agent name are spelled `newsletter_reseracher` (sic) everywhere. Keep the spelling consistent across `crew.jsonc` and `agents/` when renaming, or fix all references at once.
- Both agents use `openai/gpt-4.1` and list many built-in tools (most need API keys in `.env`, which is gitignored). Trim the lists if you only need search/scrape.
- `custom:<name>` tool refs execute `tools/<name>.py` on crew load; only run trusted code.
- `pyproject.toml` `[tool.crewai]` points at `crew.jsonc`, and the wheel only includes `agents`, `crew.jsonc`, `tools`, `knowledge`, `skills`. New top-level directories must be added to `only-include`.
- `CURSOR.md` and `GEMINI.md` are import stubs for `AGENTS.md`; keep shared guidance in `AGENTS.md`.
