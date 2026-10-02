import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from check_list import README, lint  # noqa: E402


def test_list_format_is_clean():
    assert lint(README.read_text()) == []


def test_lint_catches_bad_entries():
    bad = "## A\n\n- [x](https://example.com)\n- [y](https://e.com) - Fine.\n- [y](https://e.com) - Again.\n\n## B\n\n[go](#nowhere)\n"
    errs = " | ".join(lint(bad))
    assert "entries must look like" in errs and "same link twice" in errs and "#nowhere" in errs
