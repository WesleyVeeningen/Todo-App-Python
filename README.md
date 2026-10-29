# Todo-App-Python

A terminal todo app in Python: add and list tasks from the command line, stored in a JSON file. Small on purpose, with a clean package layout, a real CLI entry point and pytest tests.

> **Status:** work in progress. `add` and `list` work; `done` and `remove` are next.

## Setup

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Usage

```bash
todo add Buy milk      # or: python -m todo add Buy milk
todo list              # alias: todo ls
todo done 1            # not implemented yet
todo remove 1          # alias: todo rm (not implemented yet)
todo --version
```

```
$ todo add Buy milk
Added #1: Buy milk
$ todo list
[ ]   1  Buy milk
```

Tasks are stored in `~/.todo.json` by default. Use another file with `--file PATH` or the `TODO_FILE` environment variable.

## Project layout

```
todo/
  cli.py      # argparse commands
  models.py   # Task dataclass
  storage.py  # JSON file storage
tests/
```

## Tests

```bash
pytest
```
