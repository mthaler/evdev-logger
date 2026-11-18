from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol

from event_logger.event import Event


class EventHandler(Protocol):
    def handle(self, event: Event) -> None:
        """Process one event."""


class JsonlHandler:
    """Append structured events to a UTF-8 JSON Lines file."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def handle(self, event: Event) -> None:
        with self.path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(event.to_dict(), ensure_ascii=False, default=str))
            file.write("\n")
