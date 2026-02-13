## Hotfix

<!-- What bug does this fix? Link the issue. -->

Closes #

## Hotfix Decision Tree

<!-- Claude: this is urgent. Be thorough but fast. -->

### 1. Branch Convention
- [ ] Branch name matches `fix/<issue>-<slug>`
- [ ] Issue describes the bug with reproduction steps

### 2. Root Cause
<!-- Explain what caused the bug. "It was broken" is not sufficient. -->

**Root cause**:

**Affected code**:

### 3. Fix Verification
- [ ] Fix addresses the root cause (not just symptoms)
- [ ] Fix is minimal — no scope creep
- [ ] Fix does not introduce new behavior (only corrects existing)

### 4. Regression Check
- [ ] Existing tests still pass
- [ ] New test added that would have caught this bug
- [ ] Related functionality manually verified

### 5. Acceptance Criteria (from issue)

<!-- Copy from the linked issue -->

- [ ] <!-- paste from issue -->

### 6. Impact Assessment
- [ ] What else could this fix affect?
- [ ] Database changes required? If yes, migration included and idempotent
- [ ] Configuration changes required? If yes, documented

## Evidence

```
# Before fix (reproduction):

# After fix (verification):
```

## Blocked Items

None
