from abc import ABC
from dataclasses import dataclass, field

from src.domain.base.events.event import Event

from .entity import Entity


@dataclass
class AggregateRoot(Entity, ABC):
    _events: list[Event] = field(default_factory=list, init=False, repr=False, hash=False, compare=False)

    def record_event(self, event: Event) -> None:
        self._events.append(event)

    def get_events(self) -> tuple[Event]:
        return tuple(self._events)

    def clear_events(self) -> None:
        self._events.clear()

    def pull_events(self) -> tuple[Event]:
        events = self.get_events()
        self.clear_events()
        return events
