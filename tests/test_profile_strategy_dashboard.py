from __future__ import annotations

import unittest
import struct
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class StructureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.classes: set[str] = set()
        self.scripts: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if values.get("id"):
            self.ids.add(values["id"])
        self.classes.update(values.get("class", "").split())
        if tag == "script":
            self.scripts.append(values)
        if tag == "link":
            self.links.append(values)


class StrategyDashboardPageTests(unittest.TestCase):
    def test_page_contains_live_metrics_curves_and_accessible_states(self) -> None:
        html = (ROOT / "docs/strategy/index.html").read_text(encoding="utf-8")
        parser = StructureParser()
        parser.feed(html)

        expected_ids = {
            "dashboard",
            "status-label",
            "account-equity",
            "total-pnl",
            "return-pct",
            "sharpe",
            "win-rate",
            "profit-factor",
            "trade-count",
            "max-drawdown",
            "runtime",
            "equity-curve",
            "drawdown-curve",
            "empty-state",
        }
        self.assertTrue(expected_ids.issubset(parser.ids))
        self.assertTrue({"content-grid", "metrics-panel", "chart-panel"}.issubset(parser.classes))
        self.assertIn({"type": "module", "src": "./app.js"}, parser.scripts)
        self.assertTrue(any(link.get("href") == "./styles.css" for link in parser.links))
        self.assertIn("PAPER TRADING", html)
        self.assertIn("Past performance does not guarantee future results", html)
        self.assertNotIn("strategy_id", html)
        self.assertNotIn("instance_id", html)

    def test_styles_respect_reduced_motion_and_mobile_layout(self) -> None:
        css = (ROOT / "docs/strategy/styles.css").read_text(encoding="utf-8")

        self.assertIn("prefers-reduced-motion: reduce", css)
        self.assertIn("@media (max-width: 760px)", css)
        self.assertIn("metric-value--flash", css)
        self.assertIn("scan-beacon", css)
        self.assertIn("--up: #ff1744", css.lower())
        self.assertIn("--down: #00c853", css.lower())
        self.assertIn("font-family: inter, system-ui", css.lower())
        self.assertIn("max-width: 1080px", css)
        self.assertIn("grid-template-columns: minmax(0, 48fr) minmax(0, 52fr)", css)

    def test_pages_source_disables_jekyll_processing(self) -> None:
        self.assertTrue((ROOT / "docs/.nojekyll").exists())

    def test_bilingual_readmes_place_linked_preview_immediately_after_bitpro(self) -> None:
        dashboard_url = "https://shadowell.github.io/Shadowell/strategy/"
        preview = "./assets/bitpro-paper-performance.png"
        for name, bitpro_marker, following_copy in (
            ("README.md", "**BitPro · Private Product**", "I treat market-data quality"),
            ("README_CN.md", "**BitPro · 私有产品**", "我把行情数据质量"),
        ):
            text = (ROOT / name).read_text(encoding="utf-8")
            bitpro_at = text.index(bitpro_marker)
            dashboard_at = text.index(dashboard_url)
            preview_at = text.index(preview)
            following_at = text.index(following_copy)
            self.assertLess(bitpro_at, dashboard_at)
            self.assertLess(dashboard_at, preview_at)
            self.assertLess(preview_at, following_at)
            self.assertNotIn("bitpro-paper-performance.svg", text)

    def test_profile_preview_is_a_real_png_and_svg_renderer_is_removed(self) -> None:
        preview = ROOT / "assets/bitpro-paper-performance.png"
        self.assertTrue(preview.exists())
        self.assertGreater(preview.stat().st_size, 10_000)
        with preview.open("rb") as handle:
            self.assertEqual(handle.read(8), b"\x89PNG\r\n\x1a\n")
            length = struct.unpack(">I", handle.read(4))[0]
            self.assertEqual(handle.read(4), b"IHDR")
            width, height = struct.unpack(">II", handle.read(8))
        self.assertEqual(length, 13)
        self.assertGreaterEqual(width, 1000)
        self.assertLessEqual(height, 210)
        self.assertGreaterEqual(width / height, 5.1)
        self.assertIn('width="680"', (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertFalse((ROOT / "assets/bitpro-paper-performance.svg").exists())
        self.assertFalse((ROOT / "scripts/render_strategy_card.py").exists())
        self.assertFalse((ROOT / "strategy-card/example-performance.json").exists())


if __name__ == "__main__":
    unittest.main()
