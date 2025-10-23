# Algorithms on Graphs (Python)

Solutions and utilities for the **Algorithms on Graphs** course, written in Python 3.13+.

🔗 **Course**: https://www.coursera.org/learn/algorithms-on-graphs/

This repository contains Python implementations of graph algorithms from the Coursera course, organized by week and topic. It uses [**uv**](https://github.com/astral-sh/uv) for fast dependency management and reproducible environments.

## 📚 Course Content

This repository covers algorithms from the "Algorithms on Graphs" course, including:

- **Week 1**: Graph Decomposition
  - Finding an exit from a maze
  - Connected components
  - Previsit and postvisit times

- **Week 2**: Paths in Graphs
  - Breadth-first search (BFS)
  - Shortest paths
  - Dijkstra's algorithm

- **Week 3**: Paths in Graphs (continued)
  - Bellman-Ford algorithm
  - Negative cycles
  - All-pairs shortest paths

- **Week 4**: Minimum Spanning Trees
  - Kruskal's algorithm
  - Prim's algorithm
  - Union-Find data structure

---

## 📁 Project Structure

```
algorythms-on-graph-py/
├── src/algorythms_on_graph_py/          # Main package
│   ├── week1_graph_decomposition/       # Week 1 algorithms
│   ├── week2_paths_in_graphs/           # Week 2 algorithms (future)
│   └── ...
├── scripts/                             # Development utilities
│   └── format_to_snake_case.py         # Filename formatter
├── tests/                               # Test files
├── pyproject.toml                       # Project configuration
└── README.md
```

## 🛠️ Scripts

### `format_to_snake_case.py`

A pre-commit compatible script that automatically converts Python filenames to snake_case format.

**Features:**
- Automatically renames Python files to follow snake_case convention
- Respects `.gitignore` patterns
- Skips special files (`__init__.py`, `__main__.py`, etc.)
- Supports dry-run mode for previewing changes
- Integrates with pre-commit hooks

**Usage:**
```bash
# Format all Python files in the repository
python scripts/format_to_snake_case.py

# Preview changes without applying them
python scripts/format_to_snake_case.py --dry-run

# Check compliance without making changes
python scripts/format_to_snake_case.py --check

# Format only staged files
python scripts/format_to_snake_case.py --staged
```

---

## 🚀 Quick Start

### 1. Clone and enter the project
```bash
git clone git@github.com:nerewarin/algorythms-on-graph-py.git
cd algorythms-on-graph-py
```

### 2. Install dependencies
Install runtime + development tools (pytest, ruff, mypy, pre-commit):
```bash
uv sync --extra dev
```

### 3. Set up pre-commit hooks (recommended)
Automatically run code quality checks before each commit:
```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

### 4. Run the algorithms
```bash
# Example: Run the maze exit finder
uv run python -m algorythms_on_graph_py.week1_graph_decomposition.finding_an_exit_from_a_maze
```

### 5. Run tests and quality checks
```bash
# Format code
uv run ruff format

# Lint and fix issues
uv run ruff check --fix

# Type checking
uv run mypy src

# Run tests
uv run pytest -q
```

## ⚙️ Development

### Common Commands
```bash
# Code formatting and linting
uv run ruff format
uv run ruff check --fix

# Type checking
uv run mypy src

# Testing
uv run pytest
uv run pytest -v  # verbose output

# Build package
uv build

# Install in development mode
uv pip install -e .
```

### Adding New Algorithms

1. Create a new module in the appropriate week directory (e.g., `src/algorythms_on_graph_py/week2_paths_in_graphs/`)
2. Follow the naming convention: use snake_case for filenames
3. Add comprehensive docstrings and type hints
4. Include test cases
5. Update this README with the new algorithm

### Code Style

This project follows strict Python standards:
- **Type hints**: All functions must have complete type annotations
- **Formatting**: Black-style formatting with 100 character line length
- **Linting**: Ruff for fast linting and import sorting
- **Naming**: snake_case for files and functions, PascalCase for classes

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/algorithm-name`
3. Make your changes following the code style guidelines
4. Add tests for new algorithms
5. Run quality checks: `uv run pre-commit run --all-files`
6. Commit your changes: `git commit -m "Add algorithm: brief description"`
7. Push to your fork: `git push origin feature/algorithm-name`
8. Create a Pull Request

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
