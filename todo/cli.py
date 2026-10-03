import argparse

from todo import __version__
from todo.models import Task
from todo.storage import Storage


def cmd_add(args, storage: Storage) -> int:
    tasks = storage.load()
    next_id = max((t.id for t in tasks), default=0) + 1
    task = Task(id=next_id, title=" ".join(args.title))
    tasks.append(task)
    storage.save(tasks)
    print(f"Added #{task.id}: {task.title}")
    return 0


def cmd_list(args, storage: Storage) -> int:
    tasks = storage.load()
    if not tasks:
        print("No tasks yet.")
        return 0
    for t in tasks:
        mark = "x" if t.done else " "
        print(f"[{mark}] {t.id:>3}  {t.title}")
    return 0


def cmd_done(args, storage: Storage) -> int:
    # TODO: mark task args.id as done
    print("Not implemented yet.")
    return 1


def cmd_remove(args, storage: Storage) -> int:
    # TODO: remove task args.id
    print("Not implemented yet.")
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="Terminal todo app")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--file", help="path to the tasks JSON file")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("add", help="add a task")
    p.add_argument("title", nargs="+")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("list", aliases=["ls"], help="list tasks")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("done", help="mark a task as done")
    p.add_argument("id", type=int)
    p.set_defaults(func=cmd_done)

    p = sub.add_parser("remove", aliases=["rm"], help="remove a task")
    p.add_argument("id", type=int)
    p.set_defaults(func=cmd_remove)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    storage = Storage(args.file) if args.file else Storage()
    return args.func(args, storage)
