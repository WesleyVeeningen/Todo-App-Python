from todo.cli import main
from todo.storage import Storage


def test_add_and_list(tmp_path, capsys):
    path = tmp_path / "tasks.json"
    assert main(["--file", str(path), "add", "buy", "milk"]) == 0
    assert main(["--file", str(path), "list"]) == 0
    assert "buy milk" in capsys.readouterr().out
    assert len(Storage(path).load()) == 1
