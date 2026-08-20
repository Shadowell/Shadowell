# GitHub Paper Strategy Dashboard Design

## Objective

Place a reviewable BitPro Paper-performance preview directly below the BitPro project entry in both profile READMEs. The preview links to a responsive GitHub Pages dashboard that loads real public JSON from BitPro and animates metric changes without exposing internal strategy identity.

## Presentation

- The README shows a captured preview from the deployed dashboard because GitHub README sanitization does not permit an interactive iframe or JavaScript.
- The preview links to `https://shadowell.github.io/Shadowell/strategy/`.
- The live page shows Paper status, public symbols, data time, account equity, total P&L, return, Sharpe, win rate, profit factor, trade count, 30-day maximum drawdown, runtime, equity and drawdown curves.
- Numbers count from the previous value to the new value, metrics enter in sequence, curves draw on refresh, and the latest equity point carries a subtle scanning beacon.
- Reduced-motion users receive the same information without sustained animation.
- Strategy name, strategy ID, Paper instance ID, positions, orders, signals, source code and parameters never appear.

## BitPro data contract and switching

The page reads one stable alias:

```text
GET https://bitpro.notenap.com/api/public/v1/strategy-cards/github-profile
```

BitPro returns JSON with `schema_version`, `state`, `mode`, `data` and `as_of`. `data` is present only for a valid current Paper snapshot. The protected administrator route below changes the backing strategy without changing Shadowell code, Pages URL or README:

```text
PUT https://bitpro.notenap.com/api/v2/settings/public-strategy-cards/github-profile
{"strategy_id": 441}
```

BitPro validates that the target strategy exists and owns a current Paper session before replacing the mapping. A failed switch preserves the previous mapping. The public response never includes the configured ID.

## Failure and freshness

- The page refreshes every 60 seconds with `cache: no-store`.
- `stale`, `unavailable`, `not-paper`, malformed JSON and request failures clear all previous metrics and display a safe empty state.
- The public page identifies itself as Paper Trading and includes the historical-performance disclaimer.
- Fees and slippage disclosure comes from the API response.

## Verification

- Node tests cover payload normalization, metric formatting, chart coordinates and numeric easing.
- Python tests cover semantic page structure, mobile styles and reduced-motion support.
- Browser QA covers desktop and 390px layouts, live API loading, console/network state and screenshots from real deployed data.
- README placement is checked in both languages, and the preview must link to the live Pages dashboard.
