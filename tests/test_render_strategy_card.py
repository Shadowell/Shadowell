from __future__ import annotations

import copy
import sys
import unittest
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.render_strategy_card import (  # noqa: E402
    SnapshotError,
    format_runtime,
    render_svg,
    validate_snapshot,
)


NOW = datetime(2026, 8, 20, 0, 10, tzinfo=timezone.utc)


def valid_snapshot() -> dict:
    return {
        "schema_version": 1,
        "mode": "paper",
        "status": "running",
        "currency": "USDT",
        "account_equity": 102.42,
        "total_pnl": 2.42,
        "return_pct": 2.42,
        "sharpe": 0.25,
        "win_rate_pct": 51.9,
        "profit_factor": 1.13,
        "trade_count": 54,
        "max_drawdown_30d_pct": 11.4,
        "runtime_seconds": 110640,
        "symbols": ["BTC/USDT:USDT", "ETH/USDT:USDT", "SOL/USDT:USDT"],
        "equity_curve": [
            {"at": "2026-08-19T00:00:00Z", "value": 100.0},
            {"at": "2026-08-20T00:00:00Z", "value": 102.42},
        ],
        "drawdown_curve": [
            {"at": "2026-08-19T00:00:00Z", "value_pct": 0.0},
            {"at": "2026-08-20T00:00:00Z", "value_pct": -1.2},
        ],
        "includes_fees": True,
        "includes_slippage": True,
        "as_of": "2026-08-20T00:00:00Z",
    }


class SnapshotValidationTests(unittest.TestCase):
    def test_valid_paper_snapshot_is_accepted(self) -> None:
        validate_snapshot(valid_snapshot(), NOW)

    def test_missing_required_metric_is_rejected(self) -> None:
        snapshot = valid_snapshot()
        del snapshot["max_drawdown_30d_pct"]

        with self.assertRaisesRegex(SnapshotError, "max_drawdown_30d_pct"):
            validate_snapshot(snapshot, NOW)

    def test_non_paper_snapshot_is_rejected(self) -> None:
        snapshot = valid_snapshot()
        snapshot["mode"] = "live"

        with self.assertRaisesRegex(SnapshotError, "Paper"):
            validate_snapshot(snapshot, NOW)

    def test_snapshot_older_than_thirty_minutes_is_rejected(self) -> None:
        snapshot = valid_snapshot()
        snapshot["as_of"] = "2026-08-19T23:39:59Z"

        with self.assertRaisesRegex(SnapshotError, "stale"):
            validate_snapshot(snapshot, NOW)

    def test_runtime_is_formatted_without_seconds(self) -> None:
        self.assertEqual(format_runtime(110640), "1D 6H 44M")


class SvgRenderingTests(unittest.TestCase):
    def test_svg_renders_all_approved_metrics_and_disclosures(self) -> None:
        svg = render_svg(valid_snapshot(), NOW)

        for label in (
            "账户总额",
            "总盈亏",
            "收益率",
            "Sharpe",
            "胜率",
            "盈亏比",
            "交易次数",
            "30 日最大回撤",
            "运行时间",
        ):
            self.assertIn(label, svg)
        self.assertIn("PAPER TRADING", svg)
        self.assertIn("手续费与滑点已计入", svg)
        self.assertIn("PAST PERFORMANCE DOES NOT GUARANTEE FUTURE RESULTS", svg)
        ET.fromstring(svg)

    def test_svg_never_exposes_strategy_name_or_internal_id(self) -> None:
        snapshot = valid_snapshot()
        snapshot["instance_id"] = 441
        snapshot["strategy_name"] = "EMA5/20 趋势适配动态池基准版"

        svg = render_svg(snapshot, NOW)

        self.assertNotIn("441", svg)
        self.assertNotIn("instance", svg.lower())
        self.assertNotIn("EMA5/20", svg)
        self.assertNotIn("可更换策略", svg)

    def test_symbols_are_xml_escaped(self) -> None:
        snapshot = valid_snapshot()
        snapshot["symbols"] = ["BTC<&/USDT"]

        svg = render_svg(snapshot, NOW)

        self.assertIn("BTC&lt;&amp;/USDT", svg)
        ET.fromstring(svg)

    def test_negative_performance_keeps_currency_and_percent_signs(self) -> None:
        snapshot = valid_snapshot()
        snapshot["total_pnl"] = -2.42
        snapshot["return_pct"] = -2.42

        svg = render_svg(snapshot, NOW)

        self.assertIn("-$2.42", svg)
        self.assertIn("-2.42%", svg)

    def test_invalid_snapshot_renders_safe_state_without_old_metrics(self) -> None:
        snapshot = copy.deepcopy(valid_snapshot())
        snapshot["mode"] = "live"

        svg = render_svg(snapshot, NOW)

        self.assertIn("PAPER DATA UNAVAILABLE", svg)
        self.assertNotIn("$102.42", svg)
        self.assertNotIn("+2.42%", svg)
        ET.fromstring(svg)


class ProfileIntegrationTests(unittest.TestCase):
    def test_bilingual_readmes_embed_the_local_snapshot_preview(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README_CN.md").read_text(encoding="utf-8")

        self.assertIn("./assets/bitpro-paper-performance.svg", english)
        self.assertIn("Snapshot Preview", english)
        self.assertIn("not a live feed", english)
        self.assertIn("./assets/bitpro-paper-performance.svg", chinese)
        self.assertIn("快照预览", chinese)
        self.assertIn("不是实时数据", chinese)


if __name__ == "__main__":
    unittest.main()
