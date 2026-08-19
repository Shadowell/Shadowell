# GitHub Paper Strategy Card Design

## Objective

Add a reviewable BitPro Paper-strategy performance card to the bilingual GitHub profile README. The card must support changing the backing Paper instance without changing its public URL, while never displaying the strategy name or internal instance ID.

## Public presentation

- Display `BITPRO / PAPER PERFORMANCE`, an explicit `PAPER TRADING` label, running/data state, public market symbols, and the last update time.
- Display exactly these strategy-level metrics: account equity, total P&L, return, Sharpe, win rate, profit factor, trade count, 30-day maximum drawdown, and runtime.
- Display equity and drawdown curves when the source provides points.
- Do not display the strategy name, internal strategy ID, Paper instance ID, positions, orders, signals, strategy parameters, or the ID-switching mechanism.
- State whether fees and slippage are included, and show the Paper-performance risk disclaimer.

## Strategy switching

The public image URL is stable:

```text
GET https://bitpro.notenap.com/api/public/v1/strategy-cards/github-profile.svg
```

BitPro owns a protected mapping from the public alias `github-profile` to an internal Paper instance ID. Changing the mapped instance changes the card data without modifying the Shadowell README and without exposing the ID publicly.

## BitPro interface contract

The public SVG endpoint must return:

- `Content-Type: image/svg+xml; charset=utf-8`
- `Cache-Control: no-cache, max-age=60`
- `ETag` based on the metric snapshot
- `X-Strategy-Card-State: ok | stale | unavailable | not-paper`

The endpoint renders from an internal snapshot with these fields:

```json
{
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
  "symbols": ["BTC/USDT:USDT", "ETH/USDT:USDT"],
  "equity_curve": [{"at": "2026-08-19T00:00:00Z", "value": 100.0}],
  "drawdown_curve": [{"at": "2026-08-19T00:00:00Z", "value_pct": 0.0}],
  "includes_fees": true,
  "includes_slippage": true,
  "as_of": "2026-08-20T00:00:00Z"
}
```

BitPro must reject or render a safe non-performance state when the mapped source is missing, is not Paper, lacks required fields, or is stale. It must not reuse the previous successful metrics in those states.

## Shadowell implementation

- Keep a JSON Schema for the snapshot payload.
- Provide a dependency-free Python renderer that validates and escapes input, computes the display runtime, and emits the approved SVG layout.
- Store a screenshot-derived example payload without a strategy name or ID.
- Generate a local SVG preview and embed it in both READMEs for review.
- Do not push the implementation. The local preview is not described as real-time. After BitPro deploys the public SVG endpoint, replace the local image source with the stable URL and verify GitHub rendering before publishing.

## Verification

- Unit tests cover a valid payload, missing metrics, non-Paper mode, stale data, escaping, and absence of strategy names/IDs from SVG output.
- The generated SVG parses as XML and contains all nine metric labels.
- README image references resolve locally.
- Git diff contains only strategy-card implementation and profile integration files.
