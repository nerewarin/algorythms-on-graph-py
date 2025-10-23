# Algorithms on Graphs (Python)

Solutions and utilities for the **Algorithms on Graphs** course, written in Python 3.13+.
https://www.coursera.org/learn/algorithms-on-graphs/

This repository uses [**uv**](https://github.com/astral-sh/uv) for fast dependency management
and reproducible environments.

---

## 🚀 Quick Start

### 1. Clone and enter the project
```bash
git clone https://github.com/your-username/algorythms-on-graph-py.git
cd algorythms-on-graph-py
```

### 2. Sync dependencies
Install runtime + development tools (pytest, ruff, mypy, pre-commit):
```bash
uv sync --extra dev
```

### 3. Run quality checks
```bash
uv run ruff format
uv run ruff check --fix
uv run mypy src
uv run pytest -q
```

### 4. Set up pre-commit hooks
```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

## ⚙️ Development

Common commands:
```bash
uv run ruff format
uv run ruff check --fix
uv run mypy src
uv run pytest
uv build
```

---

## 🧰 Tooling

| Tool | Purpose |
|------|----------|
| [uv](https://github.com/astral-sh/uv) | Fast dependency + environment manager |
| [pytest](https://pytest.org/) | Unit testing |
| [ruff](https://docs.astral.sh/ruff/) | Linting, formatting, import sorting |
| [mypy](https://mypy-lang.org/) | Static type checking |
| [pre-commit](https://pre-commit.com/) | Git hooks for code quality |

---

## 📄 License
MIT License © 2025 Arseniy Gorbachev
