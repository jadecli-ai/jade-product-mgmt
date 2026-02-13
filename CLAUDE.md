# jade-product-mgmt — Claude Code Instructions

> Deterministic product management with decision-tree workflows.

## Decision Tree: Issue → Branch → PR → Release

Every piece of work follows this lifecycle. Claude MUST follow it exactly.

```
1. ISSUE created (from template)     → defines WHAT to build
2. BRANCH created (naming convention) → defines HOW to scope
3. WORK done on branch               → Claude follows branch context
4. PR opened (template auto-matched)  → defines DONE criteria
5. PR checklist completed             → deterministic verification
6. MERGE to main                      → release candidate
```

---

## Branch Naming Convention

Branch prefix determines the PR template and workflow. **Claude MUST use these prefixes.**

| Prefix | PR Template | Use When |
|--------|-------------|----------|
| `release/` | `release.md` | Shipping a version to production |
| `feat/` | `feature.md` | New capability or roadmap item |
| `fix/` | `hotfix.md` | Bug fix or correction |
| `docs/` | `feature.md` | Documentation changes |
| `refactor/` | `feature.md` | Code restructuring, no behavior change |
| `chore/` | `feature.md` | Maintenance, deps, CI |

### Branch Name Format

```
<prefix>/<issue-number>-<short-description>
```

Examples:
- `feat/12-entity-index-api`
- `fix/45-uuidv7-cast-error`
- `release/v1.0.0`

---

## PR Template Selection (Decision Tree)

When opening a PR, Claude MUST select the correct template based on branch prefix:

```
Is branch prefix `release/*`?
  YES → Use .github/PULL_REQUEST_TEMPLATE/release.md
  NO  → Is branch prefix `fix/*`?
    YES → Use .github/PULL_REQUEST_TEMPLATE/hotfix.md
    NO  → Use .github/PULL_REQUEST_TEMPLATE/feature.md
```

To use a specific template with `gh`:
```bash
gh pr create --template release.md   # for release/* branches
gh pr create --template hotfix.md    # for fix/* branches
gh pr create --template feature.md   # for feat/* branches (default)
```

---

## Issue Templates (Branch-Create Context)

Issues provide the context that drives branch creation. Each issue type maps to work scope:

| Issue Template | Creates Branch | Scope |
|----------------|---------------|-------|
| Roadmap Epic | `feat/<id>-<name>` | Multi-sprint initiative, broken into stories |
| Roadmap Story | `feat/<id>-<name>` | Deliverable unit, broken into tasks |
| Roadmap Task | `feat/<id>-<name>` or `fix/<id>-<name>` | Atomic work unit |

### When Claude creates a branch from an issue:

1. Read the issue body completely
2. Extract acceptance criteria
3. Name branch per convention: `<prefix>/<issue-number>-<slug>`
4. The issue body IS the specification — do not deviate

---

## Pull-Release Checklist Rules

**Claude MUST NOT mark a checklist item complete unless the condition is actually verified.**

- `[ ]` = Not started or not verified
- `[x]` = Verified with evidence (test output, command result, manual check)

If a checklist item cannot be completed, Claude MUST:
1. Leave it unchecked
2. Add a comment explaining why
3. Tag the item as blocked

---

## Roadmap Structure

```
ROADMAP.md                          # Phases, milestones, status
├── Phase 1: Foundation             # Issues #1-N
│   ├── Epic: ...                   # Issue template: roadmap-epic
│   │   ├── Story: ...             # Issue template: roadmap-story
│   │   │   ├── Task: ...         # Issue template: roadmap-task
│   │   │   └── Task: ...
│   │   └── Story: ...
│   └── Epic: ...
├── Phase 2: ...
└── Phase 3: ...
```

Each roadmap item is a GitHub Issue. Progress is tracked by issue state (open/closed).

---

## Conventional Commits

```
<type>(<scope>): <description>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `ci`, `release`

---

## Release Process (Decision Tree)

```
Ready to release?
├── Create branch: release/vX.Y.Z
├── Open PR using release.md template
├── Complete ALL checklist items:
│   ├── Version bumped?
│   ├── Changelog updated?
│   ├── All linked issues closed?
│   ├── Tests passing?
│   └── Roadmap phase updated?
├── All items checked?
│   ├── YES → Merge to main, tag vX.Y.Z
│   └── NO → Fix blocking items first
└── Post-merge: update ROADMAP.md status
```
