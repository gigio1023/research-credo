#!/usr/bin/env python3
"""Regression tests for check_tex.py. Run: python3 scripts/test_check_tex.py"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "check_tex.py"


def run(*args: str) -> tuple[int, str]:
    p = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def write(d: Path, name: str, text: str) -> Path:
    p = d / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def test_dirty_paper() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        main = write(d, "main.tex", "\\title{A Titel With Typo}\n\\author{Alice Example}\n"
                     "\\begin{abstract}We show \\method{} works.\\end{abstract}\n"
                     "\\input{sec/intro}\n% TODO in a comment must not count\n")
        write(d, "sec/intro.tex", "This is the the result.\nSee Section ?? for details..\n"
              "<<<<<<< HEAD\nTODO: fix\n\\todo{later}\nAlice Example wrote this.\n")
        code, out = run(str(main), "--blind", "--author", "Alice Example")
        assert code == 1, out
        assert "merge-conflict marker" in out, out
        assert "TODO/FIXME/XXX text" in out, out
        assert "author note macro" in out, out
        assert "doubled word: the the" in out, out
        assert "'??'" in out, out
        assert "'..' that is not an ellipsis" in out, out
        assert out.count("author name present") == 2, out  # \author line and prose line
        assert "macros: \\method" in out, out
        assert "title: A Titel With Typo" in out, out
        assert "2 file(s)" in out, out
        assert "TODO in a comment" not in out, out


def test_log_and_commented_ack() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        main = write(d, "main.tex", "\\title{T}\n%\\section*{Acknowledgments}\n% We thank ...\nBody.\n")
        log = write(d, "main.log", "LaTeX Warning: Reference `fig:x' on page 2 undefined on input line 9.\n"
                    "Package hyperref Warning: Token not allowed.\nOutput written on main.pdf.\n")
        code, out = run(str(main), "--log", str(log))
        assert code == 1, out
        assert "acknowledgments section appears commented out" in out, out
        assert out.count("build log:") == 2, out
        assert "error\t" in out and "undefined" in out, out
        code, _ = run(str(main), "--log", str(d / "missing.log"))
        assert code == 2


def test_clean_paper() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        main = write(d, "main.tex", "\\title{Clean}\n\\begin{abstract}Plain text with 3 numbers.\\end{abstract}\n"
                     "\\include{body}\n")
        write(d, "body.tex", "Ellipsis is fine... and 'that that' is skipped? no, it is reported as a warning only.\n")
        code, out = run(str(main))
        assert code == 0, out
        assert "0 error(s)" in out, out


def test_usage_errors() -> None:
    code, _ = run("/nonexistent/file.tex")
    assert code == 2
    with tempfile.TemporaryDirectory() as tmp:
        main = write(Path(tmp), "m.tex", "x")
        code, _ = run(str(main), "--blind")
        assert code == 2


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
    print("all tests passed")
