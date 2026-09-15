# Tasks: Profile Priority and Paper Strategy

**Input**: Design documents from `specs/001-profile-priority-strategy/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Regression tests are required by FR-009 and are written before implementation.

## Phase 1: Setup

**Purpose**: Confirm the existing project surface and durable development rules.

- [X] T001 Verify the current profile/dashboard structure and ignore coverage in `.gitignore`

---

## Phase 2: Foundational

**Purpose**: Encode the shared bilingual order and inventory contract before editing content.

- [X] T002 Add failing bilingual narrative-order and preserved-inventory assertions to `tests/test_profile_strategy_dashboard.py`

**Checkpoint**: The old AI-first profile must fail the new assertions.

---

## Phase 3: User Story 1 - Understand the primary profession first (Priority: P1) 🎯 MVP

**Goal**: Make big-data development the first and unmistakable professional narrative.

**Independent Test**: The title, introduction, and substantive section order in both README files
put big data before all side-research categories.

- [X] T003 [US1] Rewrite and reorder the primary-career and ongoing-research narrative in `README_CN.md`
- [X] T004 [US1] Mirror the same semantic hierarchy and section order in `README.md`
- [X] T005 [US1] Run the bilingual narrative-order assertions in `tests/test_profile_strategy_dashboard.py`

---

## Phase 4: User Story 2 - Review concrete capability evidence (Priority: P2)

**Goal**: Place verified scale and project/product outcomes lower on the page without losing evidence.

**Independent Test**: Both profiles retain four scale results and all named projects/products under
the outcomes hierarchy, with evidence boundaries intact.

- [X] T006 [US2] Organize quantified big-data and project/product proof under the outcomes section in `README_CN.md`
- [X] T007 [US2] Mirror the outcomes hierarchy and evidence boundaries in `README.md`
- [X] T008 [US2] Run preserved-inventory and bilingual-parity assertions in `tests/test_profile_strategy_dashboard.py`

---

## Phase 5: User Story 3 - See the selected live Paper evidence (Priority: P3)

**Goal**: Map the public profile card to the requested running Paper session and remove the misleading
claim that the README PNG itself refreshes.

**Independent Test**: Pre/post Paper snapshots preserve the same target session; the public alias
returns current running metrics with 20 symbols; both captions distinguish static from live.

- [X] T009 [US3] Add a failing honest-preview-caption assertion to `tests/test_profile_strategy_dashboard.py`
- [X] T010 [US3] Update the BitPro preview captions in `README_CN.md` and `README.md`
- [X] T011 [US3] Change only the protected BitPro `github-profile` alias mapping to the validated target strategy
- [X] T012 [US3] Compare the target Paper snapshot and public alias response before/after the mapping change
- [X] T013 [US3] Recapture the current linked dashboard preview in `assets/bitpro-paper-performance.png`

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Verify the complete user-visible result and prepare a scoped commit.

- [X] T014 Run Python and Node test suites plus `git diff --check` using `specs/001-profile-priority-strategy/quickstart.md`
- [X] T015 Verify the GitHub Pages dashboard visually at desktop and narrow widths using `docs/strategy/index.html`
- [X] T016 Remove the constitution Sync Impact Report and review the current-task staged scope in `.specify/memory/constitution.md`

---

## Dependencies & Execution Order

- Phase 1 precedes all feature work.
- T002 must fail against the current README order before T003-T008.
- T009 must fail against the current misleading caption before T010.
- T011 depends on the already completed read-only target search and Paper snapshot validation.
- T012 follows T011; T013 follows public-response verification in T012.
- Phase 6 follows all three user stories.

## Implementation Strategy

The MVP is User Story 1. Continue sequentially because the stories share the two README files and
the strategy-card evidence. No delegated or parallel execution is required.
