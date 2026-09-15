# Quickstart: Validate Profile Priority and Paper Strategy

1. Run `python3 -m unittest discover -s tests -p 'test_*.py'`.
2. Run `node --test tests/*.test.mjs`.
3. Run `git diff --check` and inspect the scoped diff.
4. Verify `README.md` and `README_CN.md` follow the order in
   [profile-and-card.md](./contracts/profile-and-card.md) and preserve the full inventory.
5. Read the target Paper snapshot before and after changing the protected alias. Confirm immutable
   identity/version/start fields are unchanged and no lifecycle operation occurred.
6. Read the public alias without login. Confirm `state=ok`, `mode=paper`, `status=running`, 20 symbols,
   and parity with the target snapshot's current public metrics.
7. Open the GitHub Pages dashboard at desktop and narrow widths. Confirm live values, curves, status,
   disclosure, responsive layout, and absence of internal identity.
