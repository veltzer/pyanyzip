# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pyanyzip/core.py:48` - the bzip2 branch tests `zip_type == "bzip2"`, but `_get_type` returns `"bz2"` (line 27) and `zip_types` only accepts `"bz2"` (line 17), so every `.bz2` file falls through to `ValueError("You should not be here")`; compare against `"bz2"`.

## Medium

- `src/pyanyzip/core.py:28` - `.xz` is detected (and `"xz"` is an accepted `zip_type`, line 18) but `openzip` has no xz branch, so xz files also end in `ValueError("You should not be here")`; add `lzma.open(...)` or drop xz from the detected/accepted types.
- `tests/unit_tests/test_all.py:17` - the only positive test opens a plain file (and never closes it); nothing exercises the gzip/bz2/xz paths, which is how the two bugs above went unnoticed; add small compressed fixtures under `data/` and round-trip each type.

## Low

- `src/pyanyzip/core.py:38` - argument validation uses `assert` (also line 42), which is stripped under `python -O`, letting a bad `method`/`zip_type` through; raise `ValueError` instead.
- `pyproject.toml:91` - the mypy override sets `ignore_missing_imports` for `pyanyzip.*`, the package's own modules, which only hides real import errors; remove that entry.
- `pyproject.toml:84` - `mypy_path = "src:python:scripts"` names `python` and `scripts` directories that do not exist in this repo; reduce to `src`.
- `tests/unit_tests/test_all.py:19` - uses the relative path `data/text.txt`, so the test only passes when run from the repo root (hence the debug `print(os.getcwd())` on line 18); resolve the path from `__file__` and drop the print.
