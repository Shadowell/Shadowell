import test from 'node:test';
import assert from 'node:assert/strict';

import {
  buildPolylinePoints,
  formatMetric,
  formatRuntime,
  formatSymbols,
  normalizeCardPayload,
  tweenValue,
} from '../docs/strategy/app.js';


const payload = {
  schema_version: 1,
  state: 'ok',
  mode: 'paper',
  as_of: '2026-08-20T09:30:00Z',
  data: {
    status: 'running',
    currency: 'USDT',
    account_equity: 102.4,
    total_pnl: 2.4,
    return_pct: 2.4,
    sharpe: 0.25,
    win_rate_pct: 50,
    profit_factor: 2,
    trade_count: 54,
    max_drawdown_30d_pct: 11.4,
    runtime_seconds: 110640,
    symbols: ['BTC/USDT:USDT', 'ETH/USDT:USDT'],
    equity_curve: [
      { at: '2026-08-20T08:00:00Z', value: 100 },
      { at: '2026-08-20T09:00:00Z', value: 102.4 },
    ],
    drawdown_curve: [
      { at: '2026-08-20T08:00:00Z', value_pct: 0 },
      { at: '2026-08-20T09:00:00Z', value_pct: -1.2 },
    ],
    includes_fees: true,
    includes_slippage: true,
  },
};


test('normalizes the public Paper payload without requiring internal identity', () => {
  const view = normalizeCardPayload(payload);

  assert.equal(view.state, 'ok');
  assert.equal(view.data.account_equity, 102.4);
  assert.deepEqual(view.data.symbols, ['BTC/USDT:USDT', 'ETH/USDT:USDT']);
  assert.equal('strategy_id' in view.data, false);
  assert.equal('instance_id' in view.data, false);
});


test('rejects stale or malformed payloads instead of retaining old metrics', () => {
  assert.equal(normalizeCardPayload({ ...payload, state: 'stale', data: null }).data, null);
  assert.equal(normalizeCardPayload({ ...payload, mode: 'live' }).data, null);
  assert.equal(normalizeCardPayload({ ...payload, data: { ...payload.data, account_equity: NaN } }).data, null);
});


test('formats runtime and generates bounded chart points', () => {
  assert.equal(formatRuntime(110640), '1D 6H 44M');
  assert.equal(formatMetric('account_equity', 102.4), '$102.40');
  assert.equal(formatMetric('total_pnl', 2.4), '+$2.40');
  assert.equal(formatMetric('return_pct', -2.4), '-2.40%');
  assert.equal(formatMetric('trade_count', 54), '54');
  assert.equal(buildPolylinePoints([100, 102.4], 100, 40), '0.00,40.00 100.00,0.00');
  assert.equal(buildPolylinePoints([], 100, 40), '');
});


test('summarizes large public market scopes without pushing metrics below the fold', () => {
  assert.equal(formatSymbols(['BTC', 'ETH', 'SOL'], 2), 'BTC  ·  ETH  ·  +1 MORE MARKET');
  assert.equal(formatSymbols(['BTC', 'ETH'], 10), 'BTC  ·  ETH');
});


test('numeric tween uses eased intermediate values and lands exactly on target', () => {
  assert.equal(tweenValue(10, 20, 0), 10);
  assert.equal(tweenValue(10, 20, 1), 20);
  assert.ok(tweenValue(10, 20, 0.5) > 15);
  assert.ok(tweenValue(10, 20, 0.5) < 20);
});
