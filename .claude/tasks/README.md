# Task Queue System

Persistent task queue for cross-session Claude Code workflows.

## Schema

Each line in `queued.jsonl` is a JSON object:

```json
{
  "id": "QUEUE-NNN",
  "title": "Human-readable title",
  "type": "feat|fix|docs|build|chore",
  "repo": "target-repo-slug",
  "prompt": "Reinforcement preamble + task instructions",
  "depends_on": [],
  "created": "2026-02-13",
  "status": "queued"
}
```

When popped to `flushed.jsonl`, gains:
```json
{
  "flushed_at": "2026-02-13T19:00:00Z",
  "status": "flushed"
}
```

## Usage

```bash
python3 scripts/queue.py status   # Count queued vs flushed
python3 scripts/queue.py pop      # Pop next task, print prompt
```

## Workflow

1. Queue tasks by appending to `queued.jsonl`
2. After `/clear`, run `python3 scripts/queue.py pop`
3. Claude reads the prompt and follows the PM workflow
4. Task moves to `flushed.jsonl` as audit trail

## Prompt Preamble

Every popped task prompt starts with:

> This is a pinned task from the PM queue. Follow the PM workflow:
> 1. Read CLAUDE.md in the target repo
> 2. Create a branch via conventional naming: `<type>/<issue>-<slug>`
> 3. Use conventional commits for all changes
> 4. Track progress against the roadmap
