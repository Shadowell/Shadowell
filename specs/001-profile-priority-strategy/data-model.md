# Data Model: Profile Priority and Paper Strategy

## Profile Section

- `language`: `zh-CN` or `en`
- `role`: `hero`, `primary`, `ongoing-research`, `outcomes`, or `focus`
- `order`: unique positive position within one language
- `claims`: text with an explicit evidence boundary where applicable
- `entries`: preserved projects, products, capabilities, links, or quantified results

Validation: both languages use the same role order and equivalent entry inventory. `primary` is big
data; AI, Agent, quant, and product exploration are under `ongoing-research`.

## Public Strategy Alias

- `alias`: stable public string `github-profile`
- `strategy_id`: protected mapping value; never emitted publicly
- `mode`: must resolve to `paper`

State transition: `mapped-to-current -> validate-target -> mapped-to-480`. A validation failure leaves
the original mapping unchanged.

## Paper Session Evidence

- Immutable comparison fields: instance identity, configured/started timestamps, strategy/config
  versions
- Continuity fields: status, equity, PnL, trade count, curve version, event evidence
- Public fields: status, equity, total PnL, return, Sharpe, win rate, profit factor, trade count,
  drawdown, runtime, symbols, curves, modeled cost flags, generation time

Validation: the target remains the same running Paper session before and after alias change. Public
data contains only the public field set and exactly 20 symbols for the requested strategy.

## Static README Preview

- `asset_path`: `assets/bitpro-paper-performance.png`
- `destination`: stable GitHub Pages dashboard URL
- `caption`: explicitly identifies the image as static and the destination as refreshing
