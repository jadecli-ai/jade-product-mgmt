#!/usr/bin/env python3
"""Check availability of secrets and variables without exposing values.

Usage:
    python3 scripts/check-secrets.py              # Check all scopes
    python3 scripts/check-secrets.py --env-only    # Only check local .env
    python3 scripts/check-secrets.py --gh-only     # Only check GitHub secrets/vars
    python3 scripts/check-secrets.py --json        # Output as JSON

Exit codes:
    0 = all required keys present
    1 = one or more required keys missing
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

# ── Required keys by scope ──────────────────────────────────────────────
# Add new keys here. Format: (key_name, description)

ENV_KEYS: list[tuple[str, str]] = [
    # Add local .env keys as needed for this repo
]

REPO_SECRETS: list[tuple[str, str]] = [
    # Add repo secrets as needed
]

REPO_VARIABLES: list[tuple[str, str]] = [
    # Add repo variables as needed
]

ORG_SECRETS: list[tuple[str, str]] = []
ORG_VARIABLES: list[tuple[str, str]] = []

# ── Helpers ─────────────────────────────────────────────────────────────

REPO = os.environ.get("GITHUB_REPOSITORY", "jadecli-ai/jade-product-mgmt")
ORG = REPO.split("/")[0] if "/" in REPO else "jadecli-ai"


def _check_env(keys: list[tuple[str, str]], env_file: Path | None = None) -> dict[str, bool]:
    env_vars: set[str] = set(os.environ.keys())
    if env_file and env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                env_vars.add(line.split("=", 1)[0].strip())
    return {k: k in env_vars for k, _ in keys}


def _gh_list(cmd: list[str]) -> set[str]:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        names: set[str] = set()
        for line in result.stdout.strip().splitlines():
            parts = line.split()
            if parts:
                names.add(parts[0])
        return names
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return set()


def _check_gh_secrets(keys: list[tuple[str, str]], scope: str = "repo") -> dict[str, bool]:
    if scope == "org":
        existing = _gh_list(["gh", "secret", "list", "--org", ORG])
    else:
        existing = _gh_list(["gh", "secret", "list", "--repo", REPO])
    return {k: k in existing for k, _ in keys}


def _check_gh_variables(keys: list[tuple[str, str]], scope: str = "repo") -> dict[str, bool]:
    if scope == "org":
        existing = _gh_list(["gh", "variable", "list", "--org", ORG])
    else:
        existing = _gh_list(["gh", "variable", "list", "--repo", REPO])
    return {k: k in existing for k, _ in keys}


def check_all(*, env: bool = True, gh: bool = True, env_file: Path | None = None) -> dict[str, dict[str, bool]]:
    results: dict[str, dict[str, bool]] = {}
    if env and ENV_KEYS:
        results["env"] = _check_env(ENV_KEYS, env_file)
    if gh:
        if REPO_SECRETS:
            results["repo_secrets"] = _check_gh_secrets(REPO_SECRETS, "repo")
        if REPO_VARIABLES:
            results["repo_variables"] = _check_gh_variables(REPO_VARIABLES, "repo")
        if ORG_SECRETS:
            results["org_secrets"] = _check_gh_secrets(ORG_SECRETS, "org")
        if ORG_VARIABLES:
            results["org_variables"] = _check_gh_variables(ORG_VARIABLES, "org")
    return results


def _print_table(results: dict[str, dict[str, bool]]) -> bool:
    all_ok = True
    all_keys = {k: d for k, d in ENV_KEYS + REPO_SECRETS + REPO_VARIABLES + ORG_SECRETS + ORG_VARIABLES}
    for scope, checks in results.items():
        header = scope.upper().replace("_", " ")
        print(f"\n  {header}")
        print(f"  {'─' * 50}")
        for key, present in checks.items():
            status = "OK" if present else "MISSING"
            icon = "+" if present else "x"
            desc = all_keys.get(key, "")
            print(f"  [{icon}] {key:<30} {status:<8} {desc}")
            if not present:
                all_ok = False
    return all_ok


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--env-only", action="store_true")
    parser.add_argument("--gh-only", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--env-file", type=Path, default=None)
    args = parser.parse_args()

    env_file = args.env_file
    if env_file is None:
        for candidate in [Path(".env"), Path(__file__).resolve().parent.parent / ".env"]:
            if candidate.exists():
                env_file = candidate
                break

    results = check_all(env=not args.gh_only, gh=not args.env_only, env_file=env_file)

    if not results:
        print("\n  No keys configured to check. Add keys to scripts/check-secrets.py.\n")
        return

    if args.json:
        print(json.dumps(results, indent=2))
        sys.exit(0 if all(all(v.values()) for v in results.values()) else 1)

    print(f"\n  Secrets & Variables Audit")
    print(f"  Repo: {REPO}  |  Org: {ORG}")
    all_ok = _print_table(results)
    missing = sum(1 for checks in results.values() for v in checks.values() if not v)
    total = sum(len(checks) for checks in results.values())
    print(f"\n  {total - missing}/{total} keys configured")
    if not all_ok:
        print("  Run with --json for machine-readable output\n")
        sys.exit(1)
    print()


if __name__ == "__main__":
    main()
