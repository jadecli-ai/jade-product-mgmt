---
id: "REF-INK-001"
version: "1.0.0"
type: "reference"
status: "active"
created: 2026-02-13
updated: 2026-02-13
---

# Ink Ecosystem Reference Catalog

CLI tools built on React Ink and related terminal UI frameworks.

## Tool Catalog

| Tool | Category | Description | MCP Potential |
|------|----------|-------------|---------------|
| Claude Code | AI/Dev | Agentic coding CLI (Anthropic) | n/a (integrated) |
| Gemini CLI | AI/Dev | Agentic coding CLI (Google) | high |
| tweakcc | AI/Dev | Customize Claude Code styling/themes | medium |
| Wrangler | Cloud/Infra | Cloudflare Workers CLI | high |
| Vercel CLI | Cloud/Infra | Vercel deployment and management | high |
| Netlify CLI | Cloud/Infra | Netlify deployment and management | medium |
| Prisma | Database | Unified data layer, schema migrations | high |
| Drizzle Studio | Database | Database browser and editor | medium |
| Turso CLI | Database | libSQL/SQLite edge database | medium |
| Neon CLI | Database | Serverless Postgres management | high |
| Ink | Framework | React for CLIs (base framework) | n/a (framework) |
| Pastel | Framework | Ink framework for building CLI apps | n/a (framework) |
| create-ink-app | Framework | Scaffold Ink CLI applications | low |
| Gatsby CLI | Frontend | Static site generator | low |
| Next.js CLI | Frontend | React framework CLI | medium |
| Expo CLI | Mobile | React Native development | medium |
| ESLint | Linting | JavaScript/TypeScript linting | medium |
| Prettier | Formatting | Code formatter | low |
| Vitest | Testing | Vite-native test framework | medium |
| Jest | Testing | JavaScript testing framework | medium |
| Playwright | Testing | Browser automation and testing | high |
| Cypress | Testing | E2E testing framework | medium |
| Docker CLI | DevOps | Container management | high |
| k9s | DevOps | Kubernetes TUI | medium |
| lazygit | DevOps | Git TUI | medium |
| gh CLI | DevOps | GitHub from terminal | high |
| Terraform | Infrastructure | Infrastructure as Code | high |
| Pulumi | Infrastructure | Infrastructure as Code (TypeScript) | high |
| Astro CLI | Frontend | Content-focused web framework | medium |
| Remix CLI | Frontend | Full-stack React framework | medium |
| Turborepo | Monorepo | High-performance build system | medium |
| Nx | Monorepo | Smart monorepo build orchestration | medium |
| pnpm | Package | Fast, disk-efficient package manager | low |
| Bun | Runtime | Fast JavaScript runtime and toolkit | medium |
| Deno | Runtime | Secure JavaScript/TypeScript runtime | medium |
| Sentry CLI | Monitoring | Error tracking and monitoring | high |
| Datadog CLI | Monitoring | Observability platform | high |
| Stripe CLI | Payments | Payment API testing and management | high |
| Twilio CLI | Communication | Communication API management | medium |
| Supabase CLI | Backend | Open-source Firebase alternative | high |
| Convex CLI | Backend | Reactive backend platform | medium |

## Patterns Worth Adopting

### React-in-Terminal

Ink proves that React's component model works for CLIs. Key patterns relevant to our TUI work:

- **Component composition**: Build complex TUIs from small, reusable components
- **State management**: `useState`/`useReducer` for interactive terminal UIs
- **Layout system**: Flexbox-based layout in terminal (Yoga)
- **Ink hooks**: `useInput`, `useApp`, `useStdin` for terminal interaction

### Relevance to Rich/Textual TUI

Our `scripts/tui/` uses Python's Rich/Textual instead of Ink, but the patterns translate:

| Ink Pattern | Rich/Textual Equivalent |
|-------------|------------------------|
| `<Box>` layout | `Layout`, `Panel` |
| `<Text>` styling | `Text`, `markup` |
| `<Table>` | `Table` |
| `useInput` | `Textual.on_key` |
| `useState` | `reactive` attributes |

### MCP Integration Opportunities

Tools rated "high" MCP potential could expose their capabilities as MCP servers, allowing Claude Code to:
- Deploy to Cloudflare/Vercel/Netlify directly
- Run Prisma migrations and queries
- Manage Docker containers
- Create GitHub issues/PRs
- Monitor Sentry/Datadog errors
- Process Stripe payments
