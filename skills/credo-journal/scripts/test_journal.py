#!/usr/bin/env python3
"""Regression tests for journal.py. Run: python3 scripts/test_journal.py"""
from __future__ import annotations

import datetime as dt
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "journal.py"


def run(*args: str) -> tuple[int, str, str]:
    p = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def test_append_is_append_only() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        j = Path(tmp) / "journal.md"
        code, out, _ = run("--path", str(j), "append", "--kind", "idea", "--title", "Problem A", "--field", "why=x")
        assert code == 0 and "appended" in out, out
        first = j.read_bytes()
        code, _, _ = run("--path", str(j), "append", "--kind", "prediction", "--title", "Proj", "--field", "decision=continue")
        assert code == 0
        assert j.read_bytes().startswith(first), "earlier bytes were rewritten"
        text = j.read_text()
        today = dt.date.today().isoformat()
        assert f"## {today} idea: Problem A" in text and "- why: x" in text
        assert f"## {today} prediction: Proj" in text and "- decision: continue" in text


def test_read_filters() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        j = Path(tmp) / "journal.md"
        old = (dt.date.today() - dt.timedelta(days=120)).isoformat()
        j.write_text(f"## {old} idea: Old one\n- why: y\n\n")
        run("--path", str(j), "append", "--kind", "hindsight", "--title", "New one")
        code, out, err = run("--path", str(j), "read", "--older-than", "90")
        assert code == 0 and "Old one" in out and "New one" not in out, out
        assert "1 entry shown" in err, err
        code, out, _ = run("--path", str(j), "read", "--kind", "hindsight")
        assert "New one" in out and "Old one" not in out, out


def test_usage_errors() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        j = Path(tmp) / "journal.md"
        assert run("--path", str(j), "append", "--kind", "todo", "--title", "x")[0] == 2
        assert run("--path", str(j), "append", "--kind", "idea", "--title", "x", "--field", "novalue")[0] == 2
        assert run("--path", str(j), "read")[0] == 2
        assert not j.exists(), "a failed append must not create the file"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn(); print(f"ok  {name}")
    print("all tests passed")
