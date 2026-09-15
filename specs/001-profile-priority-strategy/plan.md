# Implementation Plan: Profile Priority and Paper Strategy

**Branch**: `main` | **Date**: 2026-09-15 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/001-profile-priority-strategy/spec.md`

## Summary

Restructure both GitHub profile READMEs into a deliberate three-step narrative: big-data primary
profession, ongoing AI/Agent/quant/product side research, then verified outcomes and capability
proof. Add regression assertions for bilingual order and preserved inventory. Switch the protected
BitPro `github-profile` alias to the uniquely matched running Paper strategy 480 through the
existing settings endpoint, verify the Paper session is unchanged, and make the README caption
honest about the embedded PNG being static while the linked page refreshes.

## Technical Context

**Language/Version**: Markdown, browser JavaScript modules, CSS, Python 3, Node.js 22-compatible tests

**Primary Dependencies**: GitHub README rendering, GitHub Pages, existing BitPro public/settings APIs

**Storage**: Repository files; BitPro-owned settings and Paper persistence remain external

**Testing**: Python `unittest`, Node.js built-in test runner, public endpoint assertions, browser QA

**Target Platform**: GitHub profile README and modern desktop/mobile browsers

**Project Type**: Bilingual public profile plus static telemetry web page

**Performance Goals**: Preserve the dashboard's 60-second poll interval and compact first viewport

**Constraints**: No internal strategy identity in public artifacts; no Paper mutation; no mock data;
README images do not refresh; no push or deployment without explicit authorization

**Scale/Scope**: Two README files, one profile-card caption/image, one protected alias mapping, and
the existing dashboard regression suite

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Career Narrative First**: PASS — planned order makes big data primary and side research secondary.
- **Bilingual Parity**: PASS — matching section hierarchy and inventory are required and tested.
- **Evidence Before Claims**: PASS — all outcomes stay bounded; current Paper/public data is checked.
- **Public Privacy Boundary**: PASS — only the protected alias is changed; public payload stays cropped.
- **User-Visible Verification**: PASS — tests, endpoint checks, and desktop/mobile browser review are planned.
- **Paper continuity constraint**: PASS — pre/post snapshot comparison is mandatory; no lifecycle tool is used.

## Project Structure

### Documentation (this feature)

```text
specs/001-profile-priority-strategy/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```

### Source Code (repository root)

```text
README.md
README_CN.md
assets/
└── bitpro-paper-performance.png
docs/strategy/
├── index.html
├── styles.css
└── app.js
tests/
├── strategy-dashboard.test.mjs
└── test_profile_strategy_dashboard.py
```

**Structure Decision**: Preserve the current static profile/dashboard structure. Content changes
stay in the README pair, contract behavior stays in the existing tests, and the BitPro mapping is an
operational setting change rather than Shadowell application code.

## Complexity Tracking

No constitution violations.
