from __future__ import annotations

import argparse
import json
import math
from html import escape
from datetime import datetime, timezone
from pathlib import Path


class SnapshotError(ValueError):
    pass


REQUIRED_NUMBERS = (
    "account_equity",
    "total_pnl",
    "return_pct",
    "sharpe",
    "win_rate_pct",
    "profit_factor",
    "trade_count",
    "max_drawdown_30d_pct",
    "runtime_seconds",
)


def _parse_utc(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError) as exc:
        raise SnapshotError("as_of must be an ISO-8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise SnapshotError("as_of must include a timezone")
    return parsed.astimezone(timezone.utc)


def validate_snapshot(snapshot: dict, now: datetime) -> None:
    if not isinstance(snapshot, dict):
        raise SnapshotError("snapshot must be an object")
    if snapshot.get("mode") != "paper":
        raise SnapshotError("only Paper snapshots are allowed")
    if snapshot.get("schema_version") != 1:
        raise SnapshotError("schema_version must be 1")
    for field in REQUIRED_NUMBERS:
        value = snapshot.get(field)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise SnapshotError(f"{field} must be a finite number")
        if not math.isfinite(float(value)):
            raise SnapshotError(f"{field} must be a finite number")
    if not 0 <= float(snapshot["win_rate_pct"]) <= 100:
        raise SnapshotError("win_rate_pct must be between 0 and 100")
    if not 0 <= float(snapshot["max_drawdown_30d_pct"]) <= 100:
        raise SnapshotError("max_drawdown_30d_pct must be between 0 and 100")
    if int(snapshot["trade_count"]) != snapshot["trade_count"]:
        raise SnapshotError("trade_count must be an integer")
    if int(snapshot["runtime_seconds"]) != snapshot["runtime_seconds"]:
        raise SnapshotError("runtime_seconds must be an integer")
    if snapshot["trade_count"] < 0 or snapshot["runtime_seconds"] < 0:
        raise SnapshotError("counts and runtime must be non-negative")
    if not isinstance(snapshot.get("symbols"), list) or not all(
        isinstance(symbol, str) and symbol for symbol in snapshot["symbols"]
    ):
        raise SnapshotError("symbols must be a non-empty string array")
    if snapshot.get("status") not in {"running", "paused", "stopped"}:
        raise SnapshotError("status is invalid")
    if not isinstance(snapshot.get("currency"), str) or not snapshot["currency"]:
        raise SnapshotError("currency must be a non-empty string")
    for field, value_field in (
        ("equity_curve", "value"),
        ("drawdown_curve", "value_pct"),
    ):
        points = snapshot.get(field)
        if not isinstance(points, list):
            raise SnapshotError(f"{field} must be an array")
        for point in points:
            if not isinstance(point, dict) or not isinstance(point.get("at"), str):
                raise SnapshotError(f"{field} contains an invalid point")
            value = point.get(value_field)
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise SnapshotError(f"{field} contains an invalid value")
            if not math.isfinite(float(value)):
                raise SnapshotError(f"{field} contains an invalid value")
    for field in ("includes_fees", "includes_slippage"):
        if not isinstance(snapshot.get(field), bool):
            raise SnapshotError(f"{field} must be a boolean")
    as_of = _parse_utc(snapshot.get("as_of"))
    if now.tzinfo is None:
        raise SnapshotError("now must include a timezone")
    age_seconds = (now.astimezone(timezone.utc) - as_of).total_seconds()
    if age_seconds < -300:
        raise SnapshotError("snapshot timestamp is in the future")
    if age_seconds > 1800:
        raise SnapshotError("snapshot is stale")


def format_runtime(seconds: int) -> str:
    days, remainder = divmod(int(seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes = remainder // 60
    return f"{days}D {hours}H {minutes}M"


def _signed(value: float, suffix: str = "") -> str:
    prefix = "+" if value > 0 else ""
    return f"{prefix}{value:.2f}{suffix}"


def _money(value: float) -> str:
    if value > 0:
        return f"+${value:.2f}"
    if value < 0:
        return f"-${abs(value):.2f}"
    return "$0.00"


def _line_path(
    values: list[float],
    *,
    x: float,
    y: float,
    width: float,
    height: float,
) -> str:
    if not values:
        return ""
    if len(values) == 1:
        return f"M{x:.1f} {y + height / 2:.1f}"
    low = min(values)
    high = max(values)
    span = high - low
    if span == 0:
        span = 1.0
    points = []
    for index, value in enumerate(values):
        px = x + width * index / (len(values) - 1)
        py = y + height - ((value - low) / span) * height
        points.append((px, py))
    commands = [f"M{points[0][0]:.1f} {points[0][1]:.1f}"]
    commands.extend(f"L{px:.1f} {py:.1f}" for px, py in points[1:])
    return " ".join(commands)


def _unavailable_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360" role="img" aria-labelledby="title description">
  <title id="title">BitPro Paper performance unavailable</title>
  <desc id="description">The Paper snapshot is missing, stale, invalid, or unavailable.</desc>
  <rect width="1200" height="360" rx="24" fill="#111820" stroke="#3a495c"/>
  <text x="54" y="72" fill="#3bd7a0" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="18" font-weight="700">BITPRO / PAPER PERFORMANCE</text>
  <text x="54" y="180" fill="#f2f6fa" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="38" font-weight="700">PAPER DATA UNAVAILABLE</text>
  <text x="54" y="225" fill="#748397" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="16">No previous performance values are reused.</text>
  <text x="54" y="318" fill="#657488" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="12">PAST PERFORMANCE DOES NOT GUARANTEE FUTURE RESULTS</text>
</svg>"""


def render_svg(snapshot: dict, now: datetime) -> str:
    try:
        validate_snapshot(snapshot, now)
    except SnapshotError:
        return _unavailable_svg()

    symbols = " · ".join(snapshot["symbols"])
    if len(symbols) > 112:
        symbols = symbols[:109].rstrip() + "…"
    symbols = escape(symbols)
    status = snapshot["status"].upper()
    status_color = {
        "RUNNING": "#3bd7a0",
        "PAUSED": "#ffb37b",
        "STOPPED": "#a7b2c0",
    }[status]
    positive_color = "#ff5877" if snapshot["return_pct"] >= 0 else "#3bd7a0"
    as_of = _parse_utc(snapshot["as_of"]).strftime("%Y-%m-%d %H:%M UTC")
    fee_copy = (
        "手续费与滑点已计入"
        if snapshot["includes_fees"] and snapshot["includes_slippage"]
        else "费用口径未完整计入"
    )
    equity_path = _line_path(
        [float(point["value"]) for point in snapshot["equity_curve"]],
        x=54,
        y=492,
        width=1092,
        height=88,
    )
    drawdown_path = _line_path(
        [float(point["value_pct"]) for point in snapshot["drawdown_curve"]],
        x=54,
        y=596,
        width=1092,
        height=28,
    )

    metrics = (
        ("Sharpe", f"{snapshot['sharpe']:.2f}", "#62a8ff"),
        ("胜率", f"{snapshot['win_rate_pct']:.1f}%", "#62a8ff"),
        ("盈亏比", f"{snapshot['profit_factor']:.2f}", "#62a8ff"),
        ("交易次数", str(int(snapshot["trade_count"])), "#62a8ff"),
        ("30 日最大回撤", f"{snapshot['max_drawdown_30d_pct']:.1f}%", "#ff747c"),
        ("运行时间", format_runtime(int(snapshot["runtime_seconds"])), "#b7c1cf"),
    )
    metric_cells = []
    cell_width = 200
    for index, (label, value, color) in enumerate(metrics):
        x = index * cell_width
        metric_cells.append(
            f'<line x1="{x}" y1="328" x2="{x}" y2="448" class="line"/>'
            f'<text x="{x + 28}" y="365" class="label">{escape(label)}</text>'
            f'<text x="{x + 28}" y="411" fill="{color}" class="small-value">{escape(value)}</text>'
        )
    metric_markup = "".join(metric_cells)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="700" viewBox="0 0 1200 700" role="img" aria-labelledby="title description">
  <title id="title">BitPro Paper performance snapshot</title>
  <desc id="description">Public Paper-trading metrics without a strategy name or internal ID.</desc>
  <defs>
    <linearGradient id="equity-fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3bd7a0" stop-opacity="0.28"/><stop offset="1" stop-color="#3bd7a0" stop-opacity="0"/></linearGradient>
    <style>
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; }}
      .line {{ stroke: #2c3948; stroke-width: 1; }}
      .label {{ fill: #748397; font: 15px ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing: .5px; }}
      .big-value {{ font: 700 48px ui-monospace, SFMono-Regular, Menlo, monospace; }}
      .small-value {{ font: 700 29px ui-monospace, SFMono-Regular, Menlo, monospace; }}
    </style>
  </defs>
  <rect width="1200" height="700" rx="24" fill="#111820" stroke="#3a495c"/>
  <rect x="1" y="1" width="5" height="698" rx="2" fill="#3bd7a0"/>
  <text x="54" y="54" fill="#f2f6fa" class="mono" font-size="20" font-weight="700">BITPRO / <tspan fill="#3bd7a0">PAPER PERFORMANCE</tspan></text>
  <rect x="54" y="80" width="130" height="34" rx="17" fill="#10251f" stroke="#2fa77f"/>
  <text x="119" y="102" fill="#3bd7a0" class="mono" font-size="13" text-anchor="middle">PAPER TRADING</text>
  <circle cx="1060" cy="50" r="5" fill="{status_color}"/>
  <text x="1075" y="56" fill="{status_color}" class="mono" font-size="15" font-weight="700">{status}</text>
  <text x="1146" y="88" fill="#748397" class="mono" font-size="12" text-anchor="end">{as_of}</text>
  <text x="54" y="145" fill="#748397" class="mono" font-size="14">{symbols}</text>
  <line x1="0" y1="176" x2="1200" y2="176" class="line"/>
  <rect x="0" y="176" width="1200" height="152" fill="#0d141c"/>
  <line x1="400" y1="176" x2="400" y2="328" class="line"/><line x1="800" y1="176" x2="800" y2="328" class="line"/>
  <text x="54" y="218" class="label">账户总额</text><text x="54" y="282" fill="#62a8ff" class="big-value">${snapshot['account_equity']:.2f}</text>
  <text x="454" y="218" class="label">总盈亏</text><text x="454" y="282" fill="{positive_color}" class="big-value">{_money(snapshot['total_pnl'])}</text>
  <text x="854" y="218" class="label">收益率</text><text x="854" y="282" fill="{positive_color}" class="big-value">{_signed(snapshot['return_pct'], '%')}</text>
  <line x1="0" y1="328" x2="1200" y2="328" class="line"/>{metric_markup}<line x1="0" y1="448" x2="1200" y2="448" class="line"/>
  <rect x="0" y="448" width="1200" height="204" fill="#0d141c"/>
  <text x="54" y="479" class="label">权益 / 回撤走势</text><text x="1146" y="479" fill="#748397" class="mono" font-size="12" text-anchor="end">{fee_copy}</text>
  <line x1="54" y1="520" x2="1146" y2="520" stroke="#1e2a37"/><line x1="54" y1="565" x2="1146" y2="565" stroke="#1e2a37"/><line x1="54" y1="620" x2="1146" y2="620" stroke="#1e2a37"/>
  <path d="{equity_path} L1146 580 L54 580 Z" fill="url(#equity-fill)"/><path d="{equity_path}" fill="none" stroke="#3bd7a0" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="{drawdown_path}" fill="none" stroke="#ff747c" stroke-width="2" stroke-dasharray="7 7" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="0" y1="652" x2="1200" y2="652" class="line"/>
  <text x="54" y="681" fill="#657488" class="mono" font-size="11">PAPER TRADING · {escape(fee_copy)}</text>
  <text x="1146" y="681" fill="#657488" class="mono" font-size="11" text-anchor="end">PAST PERFORMANCE DOES NOT GUARANTEE FUTURE RESULTS</text>
</svg>"""


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the BitPro Paper card")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--now", help="ISO-8601 clock used for deterministic checks")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    snapshot = json.loads(args.input.read_text(encoding="utf-8"))
    now = _parse_utc(args.now) if args.now else datetime.now(timezone.utc)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_svg(snapshot, now), encoding="utf-8")


if __name__ == "__main__":
    main()
