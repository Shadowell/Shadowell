export const API_URL = 'https://bitpro.notenap.com/api/public/v1/strategy-cards/github-profile';
export const POLL_INTERVAL_MS = 60_000;

const NUMBER_FIELDS = [
  'account_equity',
  'total_pnl',
  'return_pct',
  'sharpe',
  'win_rate_pct',
  'profit_factor',
  'trade_count',
  'max_drawdown_30d_pct',
  'runtime_seconds',
];

export function normalizeCardPayload(payload) {
  if (!payload || payload.schema_version !== 1 || payload.mode !== 'paper' || payload.state !== 'ok') {
    return { state: payload?.state || 'unavailable', data: null, asOf: payload?.as_of || null };
  }
  const data = payload.data;
  const validNumbers = data && NUMBER_FIELDS.every((field) => Number.isFinite(Number(data[field])));
  const validSymbols = Array.isArray(data?.symbols) && data.symbols.every((symbol) => typeof symbol === 'string');
  const validCurves = Array.isArray(data?.equity_curve) && Array.isArray(data?.drawdown_curve);
  if (!validNumbers || !validSymbols || !validCurves) {
    return { state: 'unavailable', data: null, asOf: payload.as_of || null };
  }
  const publicData = Object.fromEntries(
    Object.entries(data).filter(([key]) => !['strategy_id', 'instance_id', 'strategy_name'].includes(key)),
  );
  return { state: 'ok', data: publicData, asOf: payload.as_of || null };
}

export function formatRuntime(totalSeconds) {
  const seconds = Math.max(0, Math.floor(Number(totalSeconds) || 0));
  const days = Math.floor(seconds / 86_400);
  const hours = Math.floor((seconds % 86_400) / 3_600);
  const minutes = Math.floor((seconds % 3_600) / 60);
  return `${days}D ${hours}H ${minutes}M`;
}

export function formatMetric(field, value) {
  const number = Number(value) || 0;
  if (field === 'account_equity') return `$${number.toFixed(2)}`;
  if (field === 'total_pnl') return `${number > 0 ? '+' : number < 0 ? '-' : ''}$${Math.abs(number).toFixed(2)}`;
  if (field === 'return_pct') return `${number > 0 ? '+' : ''}${number.toFixed(2)}%`;
  if (field === 'win_rate_pct' || field === 'max_drawdown_30d_pct') return `${number.toFixed(1)}%`;
  if (field === 'trade_count') return String(Math.round(number));
  if (field === 'runtime_seconds') return formatRuntime(number);
  return number.toFixed(2);
}

export function buildPolylinePoints(values, width, height) {
  if (!Array.isArray(values) || values.length === 0) return '';
  const finite = values.map(Number).filter(Number.isFinite);
  if (finite.length !== values.length) return '';
  const low = Math.min(...finite);
  const high = Math.max(...finite);
  const span = high - low || 1;
  return finite
    .map((value, index) => {
      const x = finite.length === 1 ? width / 2 : (index / (finite.length - 1)) * width;
      const y = height - ((value - low) / span) * height;
      return `${x.toFixed(2)},${y.toFixed(2)}`;
    })
    .join(' ');
}

export function tweenValue(from, to, progress) {
  const t = Math.min(1, Math.max(0, Number(progress) || 0));
  const eased = 1 - (1 - t) ** 3;
  return Number(from) + (Number(to) - Number(from)) * eased;
}

const METRIC_BINDINGS = [
  ['account-equity', 'account_equity'],
  ['total-pnl', 'total_pnl'],
  ['return-pct', 'return_pct'],
  ['sharpe', 'sharpe'],
  ['win-rate', 'win_rate_pct'],
  ['profit-factor', 'profit_factor'],
  ['trade-count', 'trade_count'],
  ['max-drawdown', 'max_drawdown_30d_pct'],
  ['runtime', 'runtime_seconds'],
];

const reducedMotion = () => globalThis.matchMedia?.('(prefers-reduced-motion: reduce)').matches ?? false;

function animateMetric(element, field, target) {
  const from = Number(element.dataset.value || 0);
  const to = Number(target) || 0;
  element.dataset.value = String(to);
  element.classList.toggle('positive', ['total_pnl', 'return_pct'].includes(field) && to >= 0);
  element.classList.toggle('negative', ['total_pnl', 'return_pct'].includes(field) && to < 0);
  element.classList.remove('metric-value--flash');
  if (from === to || reducedMotion()) {
    element.textContent = formatMetric(field, to);
    return;
  }
  const started = performance.now();
  const duration = 760;
  const frame = (now) => {
    const progress = Math.min(1, (now - started) / duration);
    element.textContent = formatMetric(field, tweenValue(from, to, progress));
    if (progress < 1) requestAnimationFrame(frame);
    else {
      element.textContent = formatMetric(field, to);
      element.classList.add('metric-value--flash');
    }
  };
  requestAnimationFrame(frame);
}

function translatePoints(points, yOffset) {
  if (!points) return '';
  return points
    .split(' ')
    .map((point) => {
      const [x, y] = point.split(',').map(Number);
      return `${x.toFixed(2)},${(y + yOffset).toFixed(2)}`;
    })
    .join(' ');
}

function animateCurve(element) {
  element.classList.remove('draw-in');
  const length = element.getTotalLength?.() || 0;
  element.style.setProperty('--curve-length', String(length));
  element.style.strokeDasharray = String(length);
  void element.getBoundingClientRect();
  element.classList.add('draw-in');
}

function renderCurves(data) {
  const equity = data.equity_curve.map((point) => Number(point.value));
  const drawdown = data.drawdown_curve.map((point) => Number(point.value_pct));
  const equityPoints = buildPolylinePoints(equity, 1000, 175);
  const drawdownPoints = translatePoints(buildPolylinePoints(drawdown, 1000, 48), 202);
  const equityCurve = document.querySelector('#equity-curve');
  const equityFill = document.querySelector('#equity-fill-line');
  const drawdownCurve = document.querySelector('#drawdown-curve');
  equityCurve.setAttribute('points', equityPoints);
  equityFill.setAttribute('points', equityPoints);
  drawdownCurve.setAttribute('points', drawdownPoints);
  animateCurve(equityCurve);
  animateCurve(drawdownCurve);

  const beacon = document.querySelector('#scan-beacon');
  const last = equityPoints.split(' ').at(-1)?.split(',').map(Number);
  if (last?.length === 2) {
    beacon.setAttribute('cx', String(last[0]));
    beacon.setAttribute('cy', String(last[1]));
    beacon.classList.add('active');
  } else {
    beacon.classList.remove('active');
  }
}

function readableTimestamp(value) {
  const parsed = new Date(value);
  if (Number.isNaN(parsed.valueOf())) return 'Timestamp unavailable';
  return `${new Intl.DateTimeFormat('en-GB', {
    dateStyle: 'medium',
    timeStyle: 'medium',
    timeZone: 'UTC',
  }).format(parsed)} UTC`;
}

function clearMetrics() {
  for (const [id] of METRIC_BINDINGS) {
    const element = document.getElementById(id);
    element.textContent = '—';
    element.dataset.value = '0';
  }
  document.querySelector('#equity-curve').setAttribute('points', '');
  document.querySelector('#drawdown-curve').setAttribute('points', '');
  document.querySelector('#equity-fill-line').setAttribute('points', '');
  document.querySelector('#scan-beacon').classList.remove('active');
}

function renderUnavailable(view) {
  const dashboard = document.querySelector('#dashboard');
  dashboard.dataset.state = view.state || 'unavailable';
  dashboard.dataset.status = 'unavailable';
  dashboard.setAttribute('aria-busy', 'false');
  document.querySelector('#status-label').textContent = (view.state || 'unavailable').replace('-', ' ').toUpperCase();
  document.querySelector('#as-of').textContent = view.asOf ? readableTimestamp(view.asOf) : 'No verified snapshot';
  document.querySelector('#empty-state').hidden = false;
  clearMetrics();
}

function renderDashboard(view) {
  if (!view.data) {
    renderUnavailable(view);
    return;
  }
  const { data } = view;
  const dashboard = document.querySelector('#dashboard');
  dashboard.dataset.state = 'ok';
  dashboard.dataset.status = data.status;
  dashboard.setAttribute('aria-busy', 'false');
  document.querySelector('#empty-state').hidden = true;
  document.querySelector('#status-label').textContent = data.status.toUpperCase();
  document.querySelector('#as-of').textContent = `VERIFIED ${readableTimestamp(view.asOf)}`;
  document.querySelector('#symbols').textContent = data.symbols.join('  ·  ');
  document.querySelector('#cost-model').textContent = data.includes_fees && data.includes_slippage
    ? 'FEES + SLIPPAGE MODELED'
    : 'COST MODEL PARTIALLY AVAILABLE';
  for (const [id, field] of METRIC_BINDINGS) {
    animateMetric(document.getElementById(id), field, data[field]);
  }
  renderCurves(data);
}

async function refreshDashboard() {
  try {
    const response = await fetch(API_URL, { cache: 'no-store', headers: { Accept: 'application/json' } });
    if (!response.ok) throw new Error(`BitPro returned ${response.status}`);
    renderDashboard(normalizeCardPayload(await response.json()));
  } catch (error) {
    console.warn('Public Paper telemetry unavailable', error);
    renderUnavailable({ state: 'unavailable', data: null, asOf: new Date().toISOString() });
  }
}

if (typeof document !== 'undefined') {
  refreshDashboard();
  globalThis.setInterval(refreshDashboard, POLL_INTERVAL_MS);
}
