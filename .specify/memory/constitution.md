# Shadowell Profile Constitution

## Core Principles

### I. Career Narrative First
The profile MUST present nine years of big-data engineering as the primary profession. AI,
Agent, quantitative, and product work MUST be framed as active secondary research or delivery
tracks. Verified outcomes and capability evidence MUST remain visible without displacing the
primary career narrative.

### II. Bilingual Parity
`README.md` and `README_CN.md` MUST preserve equivalent section order, project inventory,
evidence boundaries, links, and claims. Natural phrasing may differ by language, but neither
version may introduce a materially different professional positioning or verification status.

### III. Evidence Before Claims
Production, competition, revenue, Paper, backtest, and research claims MUST reflect current,
verifiable evidence. Paper Trading MUST remain explicitly labeled as Paper and MUST NOT be
presented as live-trading performance. Missing or stale data MUST fail closed instead of being
replaced with mock, synthetic, or remembered values.

### IV. Public Privacy Boundary
Public profile and GitHub Pages artifacts MUST NOT expose private strategy IDs, Paper instance
IDs, positions, orders, signals, parameters, credentials, source code, or private repository
contents. Strategy selection MUST remain behind the protected BitPro alias mapping; the public
endpoint and page use only the stable alias and a cropped read-only payload.

### V. User-Visible Verification
Changes MUST be verified at the layer users actually see. Content changes require bilingual
order and link assertions. Dashboard changes require automated tests plus a real browser check
at desktop and narrow widths. A changed protected mapping requires a fresh public-endpoint read;
a README preview is a static image and MUST be recaptured when its visible data is meant to match
the newly selected strategy.

## Content and Runtime Constraints

- The profile is a GitHub README pair plus a static GitHub Pages dashboard under `docs/strategy/`.
- The dashboard MUST remain read-only, responsive, keyboard accessible, and respectful of reduced
  motion preferences.
- Chinese market color semantics apply to performance: red for gains and green for losses.
- Existing independently operated products, including 配料君 and 野钓潮汐, MUST remain unless the
  user explicitly asks to remove them.
- Changes to BitPro's display alias MUST NOT reset, pause, stop, reconfigure, or otherwise mutate
  any Paper session, equity, PnL, fills, positions, curves, events, runtime, or visible history.

## Development Workflow and Quality Gates

Work follows specify -> clarify -> plan -> tasks -> analyze -> implement -> converge. The smallest
relevant automated tests MUST be added or updated before implementation when behavior changes.
Before completion, run the full relevant test suite, `git diff --check`, inspect the staged scope,
and verify the rendered or deployed user-visible result proportionate to the change. Commits MUST
contain only current-task files; push, pull request creation, deployment, and live trading require
separate explicit authorization.

## Governance

This constitution governs project-level specifications, plans, tasks, implementation, and review.
Amendments require an explicit, documented rationale and semantic-version update: MAJOR for
incompatible principle changes, MINOR for new or materially expanded principles, and PATCH for
clarifications. Every feature plan and final convergence check MUST evaluate applicable MUST rules.
Project-specific instructions and the user's current request take precedence where they are more
specific without weakening safety or evidence boundaries.

**Version**: 1.0.0 | **Ratified**: 2026-09-15 | **Last Amended**: 2026-09-15
