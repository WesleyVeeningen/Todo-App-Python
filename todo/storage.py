import json
import os
from pathlib import Path

from todo.models import Task

DEFAULT_PATH = Path(os.environ.get("TODO_FILE", Path.home() / ".todo.json"))


class Storage:
    """Stores tasks in a JSON file."""

    def __init__(self, path: Path = DEFAULT_PATH):
        self.path = Path(path)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []
        with self.path.open(encoding="utf-8") as f:
            return [Task.from_dict(item) for item in json.load(f)]

    def save(self, tasks: list[Task]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2)
