#!/usr/bin/env python3
"""Generate architecture table HTML from config.yaml.

Reads ARCHITECTURE/table/config.yaml and produces a self-contained,
sortable, filterable HTML table with dark theme.

Usage:
    python3 ARCHITECTURE/table/generate.py
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

CONFIG = Path(__file__).parent / "config.yaml"
OUTPUT = Path(__file__).parent / "table.html"


def load_config() -> dict:
    with open(CONFIG) as f:
        return yaml.safe_load(f)


def generate_html(config: dict) -> str:
    meta = config["meta"]
    components = config["components"]
    colors = config.get("colors", {})
    display = config.get("display", {})

    status_colors = colors.get("status", {})
    layer_colors = colors.get("layer", {})

    rows = ""
    for c in sorted(components, key=lambda x: (x.get("layer", ""), x.get("id", ""))):
        sc = status_colors.get(c.get("status", ""), "#8b949e")
        lc = layer_colors.get(c.get("layer", ""), "#8b949e")
        deps = ", ".join(c.get("depends_on", [])) or "—"
        rows += f"""
        <tr data-layer="{c.get('layer', '')}" data-type="{c.get('type', '')}">
            <td><code>{c['id']}</code></td>
            <td><strong>{c['name']}</strong></td>
            <td><span style="color:{lc}">{c.get('layer', '')}</span></td>
            <td><span style="color:{sc}">{c.get('status', '')}</span></td>
            <td>{c.get('version', '')}</td>
            <td><code>{c.get('file_path', '')}</code></td>
            <td>{c.get('description', '')}</td>
            <td><small>{deps}</small></td>
        </tr>"""

    layers = sorted(set(c.get("layer", "") for c in components))
    filter_buttons = '<button class="filter-btn active" data-filter="all">All</button>\n'
    for layer in layers:
        lc = layer_colors.get(layer, "#8b949e")
        filter_buttons += f'        <button class="filter-btn" data-filter="{layer}" style="border-color:{lc}">{layer}</button>\n'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{meta['name']} — Architecture</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #0d1117; color: #c9d1d9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; padding: 2rem; }}
  h1 {{ color: #58a6ff; margin-bottom: 0.5rem; }}
  .meta {{ color: #8b949e; margin-bottom: 1.5rem; }}
  .filters {{ margin-bottom: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap; }}
  .filter-btn {{ background: #161b22; color: #c9d1d9; border: 1px solid #30363d; padding: 0.4rem 0.8rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem; }}
  .filter-btn:hover {{ background: #21262d; }}
  .filter-btn.active {{ background: #21262d; border-color: #58a6ff; color: #58a6ff; }}
  table {{ width: 100%; border-collapse: collapse; }}
  th {{ text-align: left; padding: 0.6rem; background: #161b22; border-bottom: 2px solid #30363d; color: #8b949e; font-size: 0.8rem; text-transform: uppercase; cursor: pointer; }}
  th:hover {{ color: #58a6ff; }}
  td {{ padding: 0.6rem; border-bottom: 1px solid #21262d; font-size: 0.9rem; }}
  tr:hover {{ background: #161b22; }}
  tr.hidden {{ display: none; }}
  code {{ background: #161b22; padding: 0.15rem 0.4rem; border-radius: 3px; font-size: 0.85em; }}
</style>
</head>
<body>
<h1>{meta['name']}</h1>
<p class="meta">v{meta['version']} — {len(components)} components</p>

<div class="filters">
  {filter_buttons}
</div>

<table id="arch-table">
<thead>
  <tr>
    <th data-sort="id">ID</th>
    <th data-sort="name">Component</th>
    <th data-sort="layer">Layer</th>
    <th data-sort="status">Status</th>
    <th data-sort="version">Ver</th>
    <th>Path</th>
    <th>Description</th>
    <th>Dependencies</th>
  </tr>
</thead>
<tbody>
{rows}
</tbody>
</table>

<script>
document.querySelectorAll('.filter-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    document.querySelectorAll('#arch-table tbody tr').forEach(row => {{
      row.classList.toggle('hidden', filter !== 'all' && row.dataset.layer !== filter);
    }});
  }});
}});

document.querySelectorAll('th[data-sort]').forEach(th => {{
  th.addEventListener('click', () => {{
    const field = th.dataset.sort;
    const tbody = document.querySelector('#arch-table tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const dir = th.classList.contains('sort-asc') ? -1 : 1;
    document.querySelectorAll('th').forEach(h => h.classList.remove('sort-asc', 'sort-desc'));
    th.classList.add(dir === 1 ? 'sort-asc' : 'sort-desc');
    rows.sort((a, b) => {{
      const idx = Array.from(th.parentNode.children).indexOf(th);
      return a.children[idx].textContent.localeCompare(b.children[idx].textContent) * dir;
    }});
    rows.forEach(r => tbody.appendChild(r));
  }});
}});
</script>
</body>
</html>"""


def main() -> None:
    config = load_config()
    html = generate_html(config)
    OUTPUT.write_text(html)
    print(f"Generated: {OUTPUT} ({len(config['components'])} components)")


if __name__ == "__main__":
    main()
