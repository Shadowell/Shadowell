# Feature Specification: Profile Priority and Paper Strategy

**Feature Branch**: `main`
**Created**: 2026-09-15
**Status**: Draft
**Input**: Reorder the bilingual profile so big-data work is the primary profession, AI and
other work are ongoing side research, and verified outcomes appear lower as capability proof.
Replace the public BitPro profile card source with
`[合约][15M][CTA] Top20 · 微结构多空突破反马丁 · 100U` and correct the misleading static
preview behavior.

## User Scenarios & Testing

### User Story 1 - Understand the primary profession first (Priority: P1)

A profile visitor immediately understands that Jie Feng's primary profession is big-data
development and that AI, Agent, quantitative, and product work are ongoing side research.

**Independent Test**: Read either language from top to bottom and verify that the title,
introduction, and first substantive section establish big data before any AI or quantitative
research section.

**Acceptance Scenarios**:

1. **Given** the Chinese profile, **When** a visitor scans the first screen, **Then** big-data
   development is named before AI or quantitative research.
2. **Given** the English profile, **When** a visitor scans the first screen, **Then** it conveys
   the same primary-versus-secondary hierarchy as the Chinese version.
3. **Given** either profile, **When** the visitor continues downward, **Then** ongoing side
   research appears before the detailed outcomes and project evidence.

---

### User Story 2 - Review concrete capability evidence (Priority: P2)

A visitor can move from the professional narrative into verified scale, projects, Paper evidence,
and independently operated products without confusing research with production or live trading.

**Independent Test**: Verify that the outcomes section preserves the four big-data scale results,
named research/product projects, the BitPro Paper disclosure, and both mini programs.

**Acceptance Scenarios**:

1. **Given** either profile, **When** a visitor reaches the outcomes section, **Then** big-data
   scale evidence is presented before project and product evidence.
2. **Given** private or research work, **When** it is described, **Then** its evidence boundary
   remains explicit and no unverified production, revenue, competition, or live-trading claim is
   introduced.
3. **Given** the project inventory, **When** the profile is reorganized, **Then** 配料君 and
   野钓潮汐 remain present.

---

### User Story 3 - See the selected live Paper evidence (Priority: P3)

A visitor clicking the BitPro profile card sees the existing running Paper session for the exact
requested strategy, while the README makes clear that its embedded image is a static preview and
the linked dashboard is the refreshing view.

**Independent Test**: Read the protected mapping response and the public alias response after the
switch, then open the dashboard and verify it shows the requested session's current public metrics.

**Acceptance Scenarios**:

1. **Given** strategy 480 has a valid running Paper session, **When** the administrator changes the
   `github-profile` alias, **Then** the alias points to strategy 480 without configuring, starting,
   stopping, resetting, or editing that Paper session.
2. **Given** the public alias after the switch, **When** it is read without login, **Then** it
   returns a current Paper payload matching the requested session's public equity, return, trade
   count, status, and 20-symbol scope without internal identity fields.
3. **Given** the README preview, **When** a visitor reads its caption, **Then** the image is described
   as static and only the linked dashboard is described as refreshing every 60 seconds.

### Edge Cases

- If the requested strategy lacks a valid Paper session, the existing alias mapping must remain.
- If public data is stale or unavailable, the dynamic page must show its existing safe empty state.
- If the static image cannot be recaptured reliably, it must not be described as live or refreshing.
- Reordering must not remove links, disclaimers, or independently operated products.

## Requirements

### Functional Requirements

- **FR-001**: Both profile titles and introductions MUST name big-data development as the primary
  profession before AI, Agent, quantitative, or product research.
- **FR-002**: Both profiles MUST order substantive content as big-data core, ongoing side research,
  then verified outcomes and capability evidence.
- **FR-003**: Both profiles MUST keep equivalent section order, project inventory, evidence labels,
  links, and disclaimers.
- **FR-004**: The outcomes section MUST preserve the four big-data scale results, HyperTrade,
  HyperARC, Alpha, StockPro, QuantBase, BitPro, Zora, FrameLab, 配料君, and 野钓潮汐.
- **FR-005**: The BitPro preview caption MUST distinguish the static embedded image from the linked
  dashboard that refreshes every 60 seconds.
- **FR-006**: The protected `github-profile` alias MUST be switched from its current source to the
  exact requested running Paper strategy through the existing validated settings contract.
- **FR-007**: The switch MUST preserve the target Paper session's identity, status, start time,
  equity, PnL, fills, positions, curves, events, runtime, and visible history.
- **FR-008**: The public response and profile artifacts MUST NOT expose strategy IDs, Paper instance
  IDs, source code, parameters, positions, orders, or signals.
- **FR-009**: Automated tests MUST verify bilingual section ordering, preserved inventory, honest
  preview copy, and existing dashboard privacy/accessibility behavior.

### Key Entities

- **Profile narrative**: title, introduction, big-data core, ongoing research, outcomes, and focus.
- **Public strategy-card alias**: stable public name whose protected mapping selects a Paper strategy.
- **Paper evidence snapshot**: cropped metrics, symbols, curves, cost flags, state, and generation time.
- **Static README preview**: a non-refreshing image linking to the dynamic dashboard.

### Assumptions

- The requested canonical strategy is the unique strategy 480 returned by current BitPro search.
- The target's existing running Paper session is the intended evidence source; no Paper mutation is
  requested or authorized.
- GitHub README cannot execute the dashboard, so honest labeling is required even if a fresh image
  is captured once.
- Changes remain on the current `main` branch because no feature-branch hook is installed.

## Success Criteria

### Measurable Outcomes

- **SC-001**: In both languages, big data appears before AI/quant in the title, introduction, and
  section order, with 100% parity across the two profiles.
- **SC-002**: All 10 named project/product entries and all four big-data scale results remain present.
- **SC-003**: The public alias returns `state=ok`, `mode=paper`, `status=running`, exactly 20 public
  symbols, and current metrics matching the target Paper snapshot at verification time.
- **SC-004**: Zero internal identity or trading-detail fields appear in the public response or page.
- **SC-005**: The full repository test suite and content-order assertions complete with zero failures.
