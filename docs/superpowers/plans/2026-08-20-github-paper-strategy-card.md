# GitHub Paper Strategy Dashboard Implementation Plan

**Goal:** Publish a live, animated, ID-private BitPro Paper dashboard and place its linked preview below the BitPro project entry in both GitHub profile READMEs.

**Architecture:** BitPro owns the public JSON and protected alias mapping. Shadowell owns a static GitHub Pages application written in HTML, CSS and JavaScript. GitHub profile READMEs use a real deployed-page screenshot as a linked preview because README content cannot execute the dashboard.

**Spec:** `docs/superpowers/specs/2026-08-20-github-paper-strategy-card-design.md`

## Work items

- [x] Implement and test the BitPro public Paper JSON contract.
- [x] Implement and test the protected alias-to-strategy mapping.
- [x] Build the responsive Shadowell HTML dashboard with number, curve and status animations.
- [x] Add safe empty-state behavior and reduced-motion support.
- [x] Publish the Shadowell `docs/` directory with GitHub Pages.
- [ ] Deploy BitPro from merged `main` and configure the initial strategy mapping.
- [ ] Verify the deployed dashboard with real data on desktop and mobile.
- [ ] Capture a real dashboard preview, place it below BitPro in both READMEs, and remove the obsolete SVG renderer/assets/tests.
- [ ] Run complete repository checks, commit the final profile integration and verify the public GitHub profile.
