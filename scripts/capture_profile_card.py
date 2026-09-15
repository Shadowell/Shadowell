"""Capture the current public dashboard, including its unavailable state."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def main():
    server = ThreadingHTTPServer(
        ("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT / "docs"))
    )
    Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": 1120, "height": 600}, device_scale_factor=2,
                                    reduced_motion="reduce")
            # Fetch from Python so local capture does not require changing public CORS policy.
            def public_response(route):
                try:
                    response = page.request.get(route.request.url, timeout=20000)
                    route.fulfill(response=response, headers={"access-control-allow-origin": "*"})
                except Exception:
                    route.fulfill(status=503, content_type="application/json", body='{}',
                                  headers={"access-control-allow-origin": "*"})
            page.route("https://bitpro.notenap.com/api/public/v1/strategy-cards/github-profile", public_response)
            page.goto(f"http://127.0.0.1:{server.server_port}/strategy/", wait_until="networkidle")
            page.locator('#dashboard[aria-busy="false"]').wait_for(timeout=30000)
            page.locator("#dashboard").screenshot(path=str(ROOT / "assets/bitpro-paper-performance.png"),
                                                   animations="disabled")
            browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
