# repodoc-demo-bugs

> ⚠️ **Notice**: This repository is **intentionally broken for demos**. It contains deliberately planted bugs, anti-patterns, and guardrail violations designed to test and benchmark automated AI bug-fixing and code review tools.

---

## Intentional Bugs Ground Truth

### A. Guardrail Violations

| # | Bug | File | Line(s) | What's Wrong | Expected Fix |
|---|---|---|---|---|---|
| A1 | Hardcoded Credentials | `app/payment_provider.py` | 5–6 | Hardcoded fake credentials (`API_KEY = "DEMO_KEY_NOT_REAL_abc123"` and `ADMIN_PASSWORD = "DEMO_PASSWORD_NOT_REAL"`). | Read credentials securely from environment variables (`os.environ` / `os.getenv`). |
| A2 | Dangerous `eval()` | `app/payment_provider.py` | 30 | `eval(rule_str)` executes arbitrary expressions from user input. | Replace with a safe parser or `ast.literal_eval`. |
| A3 | Debug prints & FIXME/TODO | Multiple (`app/payment_provider.py`, `app/orders.py`, `app/users.py`, `app/utils.py`) | Various | Unfiltered `print()` statements and unaddressed `# TODO` / `# FIXME` markers in code. | Replace with structured logging (`logging` module) and resolve TODOs. |

### B. Logic Bugs (Test-Catchable)

| # | Bug | File | Line | What's Wrong | Expected Fix |
|---|---|---|---|---|---|
| B4 | Off-by-one Slice | `app/orders.py` | 13 | `orders[0 : limit - 1]` returns only `limit - 1` items instead of `limit`. | Change slice to `orders[0 : limit]`. |
| B5 | Wrong Operator | `app/orders.py` | 23 | `price - (discount_percent / 100.0)` subtracts instead of multiplying price. | Change operator to `*`: `price * (discount_percent / 100.0)`. |
| B6 | Division by Zero | `app/orders.py` | 35 | `total / len(items)` raises `ZeroDivisionError` when `items` is an empty list (`[]`). | Guard with `if not items: return 0.0`. |
| B7 | SQL Injection | `app/users.py` | 15 | SQL query constructed via f-string formatting (`f"... WHERE email = '{email}'"`). | Use parameterized queries: `cursor.execute("... WHERE email = ?", (email,))`. |
| B8 | Mutable Default Argument | `app/utils.py` | 5 | `def add_item_to_cart(item, cart=[])` persists state across function calls. | Use `cart: Optional[List[str]] = None` and initialize inside function. |
| B9 | Unclosed File / Resource Leak | `app/users.py` | 30 | `open(...)` called without a `with` statement and without calling `close()`. | Use context manager: `with open(...) as f:`. |
| B10 | Missing None Check | `app/orders.py` | 45 | If `order["customer"]` is `None`, calling `.get(...)` raises `AttributeError`. | Add guard: `if not customer_info: return "Unknown"`. |

---

## Running Verification

### 1. Pytest
Run pytest to verify the 4 expected failing tests (B4, B5, B6, B8) and 5 passing tests:

```bash
pytest
```

Expected output: `4 failed, 5 passed`

### 2. Flake8
Run flake8 to verify style and unused import violations:

```bash
flake8 .
```

---

## License

MIT
