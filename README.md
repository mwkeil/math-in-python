# Math in Python

Personal notebook of algorithms and equations implemented in Python.
Each module is a self-contained, tested implementation with a docstring header
(idea, complexity, when to use).

![CI](https://github.com/mwkeil/math-in-python/actions/workflows/ci.yml/badge.svg)

## Index

<!-- INDEX:START -->
| Topic | Module | Complexity |
|---|---|---|
| Kalman filter (1D, constant state) | [`numerical/kalman_filter_1d`](src/math_in_python/numerical/kalman_filter_1d.py) | O(1) time and space per measurement. |
<!-- INDEX:END -->

## Layout

```
src/math_in_python/<domain>/<topic>.py   # implementation + docstring header
tests/<domain>/test_<topic>.py           # pytests
notebooks/                               # exploratory
docs/                                    # longer write ups
scripts/regenerate_index.py              # regenerates the above index
```

## Setup

```bash
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
pytest
python scripts/regenerate_index.py
```

## Adding a topic

1. Create `src/math_in_python/<domain>/<topic>.py` using the docstring template
   (title, equation/idea, complexity, when to use)
2. Add a test `tests/<domain>/test_<topic>.py`
3. Run `python scripts/regenerate_index.py` and commit
