# Product Roadmap

> jadecli-ai product roadmap with phased delivery milestones.
>
> Each item is a GitHub Issue. Status tracks automatically via issue state.

## How to Use This Roadmap

1. **Add work**: Create an issue using Epic → Story → Task templates
2. **Track progress**: Items checked off when their GitHub Issue closes
3. **Release**: When a phase milestone is complete, create a `release/vX.Y.Z` PR

---

## Phase 1: Foundation

**Goal**: Core infrastructure, entity model, CI/CD pipelines

**Milestone**: `v0.1.0` | **Status**: In Progress

### Epics

- [ ] **Neon Specialist Agent** — Document caching with pgvector, semantic search ([jadecli-ai/pm#11](https://github.com/jadecli-ai/pm/pull/11))
  - [x] V001 initial schema (pgvector, crawled_documents, chunks, queue)
  - [x] V002 bytea cast fix
  - [x] V003 entity_index with event sourcing
  - [x] CI/CD: branch-per-PR, schema diff, Claude Code action
  - [x] Secrets/variables audit tooling
  - [ ] Production branch migration
  - [ ] Backfill existing documents

- [ ] **Product Management System** — This repo, templates, workflows
  - [x] Repo creation and structure
  - [x] Issue templates (Epic, Story, Task)
  - [x] PR templates (Feature, Release, Hotfix)
  - [x] Decision tree workflow (CLAUDE.md)
  - [ ] GitHub Projects board integration
  - [ ] Automated roadmap status updates

---

## Phase 2: Integration

**Goal**: Cross-repo workflows, team automation, dashboards

**Milestone**: `v0.2.0` | **Status**: Planned

### Epics

- [ ] **Cross-Repo Orchestration** — Unified workflows across jadecli-ai repos
- [ ] **Team Dashboard** — Real-time project status visualization
- [ ] **Claude Code Agent Workflows** — `@claude` driven issue triage and PR review

---

## Phase 3: Scale

**Goal**: Multi-team support, advanced analytics, self-improving workflows

**Milestone**: `v1.0.0` | **Status**: Planned

### Epics

- [ ] **Multi-Team Routing** — Agent-driven work assignment across teams
- [ ] **Analytics Pipeline** — Entity event data → insights
- [ ] **Workflow Evolution** — Templates that improve based on completion data

---

## Release History

| Version | Date | Phase | Notes |
|---------|------|-------|-------|
| — | — | — | No releases yet |
