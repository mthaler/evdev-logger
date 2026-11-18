from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from event_logger.event import Event, EventLevel
from event_logger.handlers import EventHandler


class EventLogger:
    """Create structured events and dispatch them to configured handlers."""

    def __init__(
        self,
        handlers: Iterable[EventHandler] = (),
        source: str | None = None,
    ) -> None:
        self._handlers = list(handlers)
        self.source = source

    def log(
        self,
        level: EventLevel,
        name: str,
        **data: Any,
    ) -> Event:
        event = Event(name=name, level=level, source=self.source, data=data)
        for handler in self._handlers:
            handler.handle(event)
        return event

    def debug(self, name: str, **data: Any) -> Event:
        return self.log(EventLevel.DEBUG, name, **data)

    def info(self, name: str, **data: Any) -> Event:
        return self.log(EventLevel.INFO, name, **data)

    def warning(self, name: str, **data: Any) -> Event:
        return self.log(EventLevel.WARNING, name, **data)

    def error(self, name: str, **data: Any) -> Event:
        return self.log(EventLevel.ERROR, name, **data)

    def critical(self, name: str, **data: Any) -> Event:
        return self.log(EventLevel.CRITICAL, name, **data)
