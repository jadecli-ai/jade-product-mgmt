#!/usr/bin/env python3
"""Architecture table TUI using Rich.

Reads ARCHITECTURE/table/config.yaml and renders a colored table.

Usage:
    python3 scripts/tui/arch_table.py                  # All components
    python3 scripts/tui/arch_table.py --layer backend   # Filter by layer
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml
from rich.console import Console
from rich.table import Table

CONFIG = Path(__file__).resolve().parent.parent.parent / "ARCHITECTURE" / "table" / "config.yaml"
FALLBACK = Path(__file__).resolve().parent.parent.parent / "architecture.json"

STATUS_STYLES = {
    "active": "green",
    "in_progress": "yellow",
    "pending": "dim",
    "deprecated": "red strikethrough",
}

LAYER_STYLES = {
    "frontend": "blue",
    "middleware": "magenta",
    "backend": "green",
    "data": "yellow",
}


def load_components() -> list[dict]:
    if CONFIG.exists():
        with open(CONFIG) as f:
            return yaml.safe_load(f).get("components", [])
    if FALLBACK.exists():
        with open(FALLBACK) as f:
            data = json.load(f)
            return data.get("components", [])
    return []


def main() -> None:
    parser = argparse.ArgumentParser(description="Architecture table TUI")
    parser.add_argument("--layer", type=str, default=None, help="Filter by layer")
    args = parser.parse_args()

    components = load_components()
    if args.layer:
        components = [c for c in components if c.get("layer") == args.layer]

    components.sort(key=lambda c: (c.get("layer", ""), c.get("id", "")))

    table = Table(title="Architecture Components", show_lines=True)
    table.add_column("ID", style="cyan", width=25)
    table.add_column("Component", style="bold", width=22)
    table.add_column("Layer", width=12)
    table.add_column("Type", width=10)
    table.add_column("Status", width=10)
    table.add_column("Ver", width=6)
    table.add_column("Description", width=40)

    for c in components:
        layer_style = LAYER_STYLES.get(c.get("layer", ""), "white")
        status_style = STATUS_STYLES.get(c.get("status", ""), "white")
        table.add_row(
            c.get("id", ""),
            c.get("name", ""),
            f"[{layer_style}]{c.get('layer', '')}[/]",
            c.get("type", ""),
            f"[{status_style}]{c.get('status', '')}[/]",
            c.get("version", ""),
            c.get("description", ""),
        )

    console = Console()
    console.print(table)
    console.print(f"\n  {len(components)} components", style="dim")


if __name__ == "__main__":
    main()
