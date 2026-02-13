#!/usr/bin/env python3
"""Task queue CLI for cross-session Claude Code workflows.

Usage:
    python3 scripts/queue.py status   # Show queue counts and pending tasks
    python3 scripts/queue.py pop      # Pop next available task, print prompt
    python3 scripts/queue.py list     # List all queued tasks
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

TASKS_DIR = Path(__file__).resolve().parent.parent / ".claude" / "tasks"
QUEUED = TASKS_DIR / "queued.jsonl"
FLUSHED = TASKS_DIR / "flushed.jsonl"


def _load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    entries = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if line:
            entries.append(json.loads(line))
    return entries


def _write_jsonl(path: Path, entries: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(e) for e in entries) + "\n" if entries else "")


def _flushed_ids(flushed: list[dict]) -> set[str]:
    return {e["id"] for e in flushed}


def cmd_status() -> None:
    queued = _load_jsonl(QUEUED)
    flushed = _load_jsonl(FLUSHED)
    fids = _flushed_ids(flushed)

    print(f"\n  Task Queue Status")
    print(f"  {'─' * 40}")
    print(f"  Queued:  {len(queued)}")
    print(f"  Flushed: {len(flushed)}")
    print()

    if queued:
        for t in queued:
            deps = t.get("depends_on", [])
            blocked = [d for d in deps if d not in fids]
            status = "BLOCKED" if blocked else "READY"
            icon = "x" if blocked else ">"
            dep_str = f" (waiting: {', '.join(blocked)})" if blocked else ""
            print(f"  [{icon}] {t['id']} {t['title']:<45} [{t['type']}] {status}{dep_str}")
        print()
    else:
        print("  No tasks queued.\n")


def cmd_list() -> None:
    queued = _load_jsonl(QUEUED)
    if not queued:
        print("No tasks queued.")
        return
    for t in queued:
        print(f"{t['id']}: {t['title']} [{t['type']}] repo={t['repo']}")


def cmd_pop() -> None:
    queued = _load_jsonl(QUEUED)
    flushed = _load_jsonl(FLUSHED)
    fids = _flushed_ids(flushed)

    # Find first task whose dependencies are all flushed
    target = None
    target_idx = None
    for i, t in enumerate(queued):
        deps = t.get("depends_on", [])
        if all(d in fids for d in deps):
            target = t
            target_idx = i
            break

    if target is None:
        print("No tasks available (all blocked or queue empty).")
        sys.exit(1)

    # Move to flushed
    target["flushed_at"] = datetime.now(timezone.utc).isoformat()
    target["status"] = "flushed"
    flushed.append(target)

    queued.pop(target_idx)
    _write_jsonl(QUEUED, queued)
    _write_jsonl(FLUSHED, flushed)

    # Print the prompt for Claude
    print(f"=== Popped: {target['id']} — {target['title']} ===")
    print(f"Repo: {target['repo']}")
    print(f"Type: {target['type']}")
    print()
    print(target["prompt"])
    print()


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "status":
        cmd_status()
    elif cmd == "pop":
        cmd_pop()
    elif cmd == "list":
        cmd_list()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
