# GitHub Paper Strategy Card Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a locally reviewable, ID-private BitPro Paper-performance SVG card and prepare the stable BitPro interface contract.

**Architecture:** A strict JSON snapshot contract feeds a dependency-free Python SVG renderer. The profile initially embeds a generated local preview; the final public deployment will replace that source with BitPro's stable alias endpoint, whose internal instance mapping can change without exposing an ID.

**Tech Stack:** Python 3 standard library, JSON Schema, SVG, `unittest`, Markdown.

**Spec:** `docs/superpowers/specs/2026-08-20-github-paper-strategy-card-design.md`

## Global Constraints

- The card is Paper-only.
- Never render a strategy name or internal ID.
- Render all nine approved metrics.
- Invalid, stale, or non-Paper input must not render performance values.
- Do not push; finish with a local commit for user review.

---

### Task 1: Snapshot contract and validation

**Files:**
- Create: `strategy-card/performance.schema.json`
- Create: `strategy-card/example-performance.json`
- Create: `scripts/render_strategy_card.py`
- Test: `tests/test_render_strategy_card.py`

**Interfaces:**
- Consumes: JSON objects matching `performance.schema.json`.
- Produces: `validate_snapshot(snapshot: dict, now: datetime) -> None` and `format_runtime(seconds: int) -> str`.

- [ ] Write tests that reject missing metrics, `mode != "paper"`, snapshots older than 30 minutes, and unsafe strings.
- [ ] Run `python3 -m unittest tests.test_render_strategy_card -v` and confirm the new tests fail because the renderer does not exist.
- [ ] Implement schema-aligned validation, UTC timestamp parsing, XML escaping, and runtime formatting using only the Python standard library.
- [ ] Run the focused tests and confirm they pass.

### Task 2: Approved SVG rendering

**Files:**
- Modify: `scripts/render_strategy_card.py`
- Modify: `tests/test_render_strategy_card.py`
- Create: `assets/bitpro-paper-performance.svg`

**Interfaces:**
- Consumes: a validated snapshot dictionary.
- Produces: `render_svg(snapshot: dict, now: datetime) -> str` and CLI arguments `--input`, `--output`, and optional `--now`.

- [ ] Write tests asserting all nine labels, Paper disclosure, curves, and the absence of `instance_id`, strategy names, and switching copy.
- [ ] Run the focused tests and confirm they fail before SVG rendering exists.
- [ ] Implement the approved V3 layout with a generic identity, responsive fixed SVG viewport, escaped symbols, signed number formatting, and safe no-data rendering.
- [ ] Generate the review asset with `python3 scripts/render_strategy_card.py --input strategy-card/example-performance.json --output assets/bitpro-paper-performance.svg --now 2026-08-20T00:10:00Z`.
- [ ] Parse the generated SVG with `xml.etree.ElementTree` and run all unit tests.

### Task 3: Bilingual profile integration and local delivery

**Files:**
- Modify: `README.md`
- Modify: `README_CN.md`
- Test: `tests/test_render_strategy_card.py`

**Interfaces:**
- Consumes: `assets/bitpro-paper-performance.svg`.
- Produces: one local preview section in each profile README.

- [ ] Add tests that both READMEs reference the local SVG and label it as a Paper snapshot preview rather than real-time data.
- [ ] Add the compact performance-card section below the BitPro project entry in both READMEs.
- [ ] Run `python3 -m unittest discover -s tests -v`, `git diff --check`, and an XML parse check.
- [ ] Inspect the SVG visually, review the complete diff, and verify that no strategy name or ID appears in public output.
- [ ] Commit only the implementation files with `git commit -m "feat: add reviewable Paper strategy card"`; do not push.
