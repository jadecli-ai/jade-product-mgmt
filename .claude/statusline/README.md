# Claude Code Statusline Config

Version-controlled field definitions for the Claude Code statusline.

## Setup

1. The `config.yaml` in this directory defines the field keys and sources
2. Set your `base_path` in `.claude/settings.local.json` (not tracked):

```json
{
  "statusline": {
    "base_path": "/home/alex-jadecli/projects/refs/jadecli-ai"
  }
}
```

## Fields

| Field | Source | Description |
|-------|--------|-------------|
| `branch` | git | Current branch name |
| `untracked_count` | git | Count of untracked files (`?`) |
| `staged_count` | git | Count of staged files (`+`) |
| `modified_count` | git | Count of modified files (`~`) |
| `pr_status` | gh | PR state (OPEN/CLOSED/MERGED/local-only) |
| `last_commit_type` | git | Conventional commit type from last commit |
| `plugin_active` | file | Active plugin name |
| `pipeline_stage` | file | Current pipeline phase |

## Display Format

```
main | 2~ 1+ 0? | PR:OPEN | [feat] research
```

## Guardrails

Warnings trigger when:
- More than 5 untracked files
- Staged changes but no PR open
- Last commit doesn't use conventional format
