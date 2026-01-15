from typing import List, Dict, Any

class Memory:
    """Bounded in-memory event store."""

    def __init__(self, max_size: int = 100) -> None:
        self.max_size = max_size
        self._events: List[Dict[str, Any]] = []

    def add(self, event: Dict[str, Any]) -> None:
        self._events.append(event)
        if len(self._events) > self.max_size:
            self._events.pop(0)

    def all(self) -> List[Dict[str, Any]]:
        return list(self._events)
