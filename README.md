# newsletter_crew

A crewAI project using JSON-first configuration.

## Setup (how this project was created)

```powershell
# Install uv (Windows)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install the CrewAI CLI and confirm it is listed
uv tool install crewai
uv tool list

# Scaffold the project
crewai create crew newsletter_crew
```

## Running

```bash
crewai run
```

## Project Structure

- `agents/` - Agent definitions (JSONC)
- `crew.jsonc` - Crew definition with tasks and configuration
- `tools/` - Custom tools (Python)
- `knowledge/` - Knowledge files for agents

> **Note:** `custom:<name>` tool references execute `tools/<name>.py` as local
> Python code when the crew loads. Only run crew projects from sources you
> trust.
