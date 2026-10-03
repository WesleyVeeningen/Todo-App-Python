# Todo-App-Python

A simple terminal todo app (work in progress).

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

```bash
todo add Buy milk      # or: python -m todo add Buy milk
todo list
todo done 1            # TODO
todo remove 1          # TODO
```

Tasks are stored in `~/.todo.json` by default. Override with `--file PATH` or the `TODO_FILE` env var.

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
