"""Kickoff callbacks referenced from crew.jsonc.

before_kickoff remembers the topic; after_kickoff saves the finished newsletter as
newsletter_<Topic>_<YYYYMMDD>_<HHMMSS>.md in the folder the crew was run from.
The name uses only letters and digits plus the underscores in that pattern.
The topic travels through an environment variable because the two callbacks are
loaded separately and cannot share module state.
"""
import os
import re
from datetime import datetime
from pathlib import Path

_TOPIC_ENV = "NEWSLETTER_TOPIC"


def _topic_slug(topic: str) -> str:
    """'AI agents & tools!' -> 'AIAgentsTools': words joined, no spaces or symbols."""
    words = re.findall(r"[A-Za-z0-9]+", topic)
    return "".join(w[:1].upper() + w[1:] for w in words) or "topic"


def before_kickoff(inputs):
    os.environ[_TOPIC_ENV] = str((inputs or {}).get("topic", ""))
    return inputs


def after_kickoff(output):
    now = datetime.now()
    name = f"newsletter_{_topic_slug(os.environ.get(_TOPIC_ENV, ''))}_{now:%Y%m%d}_{now:%H%M%S}.md"
    path = Path.cwd() / name
    path.write_text(output.raw, encoding="utf-8")
    print(f"\nNewsletter saved to {path}")
    return output
