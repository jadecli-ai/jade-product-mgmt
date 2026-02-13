## Release: vX.Y.Z

<!-- Replace X.Y.Z with actual version -->

## Release Decision Tree

<!-- Claude: EVERY item must be checked with evidence. No exceptions. -->

### 1. Pre-Release Verification
- [ ] Branch name is `release/vX.Y.Z`
- [ ] All features for this release are merged to this branch
- [ ] No open PRs blocking this release

### 2. Version & Changelog
- [ ] Version bumped in all relevant files (package.json, pyproject.toml, etc.)
- [ ] CHANGELOG.md updated with all changes since last release
- [ ] Version follows SemVer:
  - MAJOR: breaking changes
  - MINOR: new features, backward compatible
  - PATCH: bug fixes only

### 3. Roadmap Alignment
- [ ] All issues linked to this release milestone are closed
- [ ] ROADMAP.md phase/milestone status updated
- [ ] No roadmap items left in "in progress" for this release

### 4. Quality Gates
- [ ] All CI checks passing
- [ ] Tests pass locally and in CI
- [ ] No known regressions
- [ ] Security: no secrets in codebase (`scripts/check-secrets.py` if available)

### 5. Database (if applicable)
- [ ] Migrations are idempotent and tested
- [ ] Schema changes documented
- [ ] Rollback plan documented (or migration is backward compatible)

### 6. Integration
- [ ] Dependent services notified (if any)
- [ ] API compatibility verified (if any)
- [ ] Environment variables documented in .env.example

### 7. Post-Merge Actions
<!-- These are done AFTER merge, not before -->
- [ ] Tag created: `git tag vX.Y.Z && git push --tags`
- [ ] GitHub Release created with changelog
- [ ] ROADMAP.md marked as released
- [ ] Notify stakeholders

## Changes Included

<!-- List all PRs/commits included in this release -->

| PR | Title | Type |
|----|-------|------|
| #N | ... | feat/fix/docs |

## Evidence

```
# test output, CI links, migration results
```

## Rollback Plan

<!-- How to revert if something goes wrong -->

```
git revert <merge-commit>
# or: revert migration V00X
```
