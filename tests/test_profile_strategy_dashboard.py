from __future__ import annotations

import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class StructureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.scripts: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if values.get("id"):
            self.ids.add(values["id"])
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

    def test_pages_source_disables_jekyll_processing(self) -> None:
        self.assertTrue((ROOT / "docs/.nojekyll").exists())


if __name__ == "__main__":
    unittest.main()
