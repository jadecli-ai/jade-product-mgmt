# jade-product-mgmt

Product management roadmap for [jadecli-ai](https://github.com/jadecli-ai) with deterministic Claude Code workflows.

## How It Works

Every piece of work follows a structured lifecycle:

**Issue** (what to build) → **Branch** (scoped work) → **PR** (done checklist) → **Merge** (release)

Templates enforce this at every step:
- **Issue templates** define the work and acceptance criteria
- **Branch naming** maps to PR template selection
- **PR templates** provide checklists Claude must complete before merge
- **ROADMAP.md** tracks phase/milestone progress

## Quick Start

1. Create an issue using a template (Epic, Story, or Task)
2. Create a branch: `feat/<issue-number>-<description>`
3. Do the work
4. Open PR — template auto-matches based on branch prefix
5. Complete the checklist
6. Merge

## Templates

| Template | Trigger |
|----------|---------|
| [Roadmap Epic](.github/ISSUE_TEMPLATE/roadmap-epic.yml) | New multi-sprint initiative |
| [Roadmap Story](.github/ISSUE_TEMPLATE/roadmap-story.yml) | Deliverable unit of work |
| [Roadmap Task](.github/ISSUE_TEMPLATE/roadmap-task.yml) | Atomic work item |
| [Feature PR](.github/PULL_REQUEST_TEMPLATE/feature.md) | `feat/*`, `docs/*`, `refactor/*`, `chore/*` branches |
| [Release PR](.github/PULL_REQUEST_TEMPLATE/release.md) | `release/*` branches |
| [Hotfix PR](.github/PULL_REQUEST_TEMPLATE/hotfix.md) | `fix/*` branches |

## Roadmap

See [ROADMAP.md](ROADMAP.md) for current phases and milestones.
