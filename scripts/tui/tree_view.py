#!/usr/bin/env python3
"""Rich file tree TUI with color-coded directories.

Usage:
    python3 scripts/tui/tree_view.py [path]
"""

from __future__ import annotations

import sys
from pathlib import Path

from rich.console import Console
from rich.tree import Tree

DIR_COLORS = {
    "agents": "bright_magenta",
    "entities": "yellow",
    "lib": "green",
    "scripts": "cyan",
    "docs": "blue",
    "tests": "red",
    ".github": "bright_black",
    ".claude": "bright_black",
    "ARCHITECTURE": "bright_yellow",
}

SKIP = {".git", ".venv", "node_modules", "__pycache__", ".mypy_cache", ".ruff_cache"}


def _dir_style(name: str) -> str:
    return DIR_COLORS.get(name, "white")


def _add_path(tree: Tree, path: Path, depth: int = 0, max_depth: int = 4) -> None:
    if depth > max_depth:
        return

    entries = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    for entry in entries:
        if entry.name in SKIP:
            continue
        if entry.is_dir():
            style = _dir_style(entry.name)
            branch = tree.add(f"[bold {style}]{entry.name}/[/]")
            _add_path(branch, entry, depth + 1, max_depth)
        else:
            icon = "📄" if entry.suffix == ".md" else "📦" if entry.suffix in (".py", ".js", ".ts") else "📋" if entry.suffix in (".yml", ".yaml") else "·"
            tree.add(f"{icon} {entry.name}")


def main() -> None:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    target = target.resolve()

    tree = Tree(f"[bold bright_blue]{target.name}/[/]")
    _add_path(tree, target)

    console = Console()
    console.print(tree)


if __name__ == "__main__":
    main()
