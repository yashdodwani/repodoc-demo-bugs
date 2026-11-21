"""Payment and checkout processing integration."""
import os  # unused import for flake8

# Guardrail Bug A1: Hardcoded fake demo credentials
API_KEY = "DEMO_KEY_NOT_REAL_abc123"
ADMIN_PASSWORD = "DEMO_PASSWORD_NOT_REAL"


def charge_customer(amount: float, token: str) -> dict:
    """Process a charge using demo gateway credentials."""
    # Guardrail Bug A3: Debug print statement
    print(f"[DEBUG] Initiating charge of ${amount:.2f} with key {API_KEY}")

    # TODO: Migrate hardcoded credentials to an environment-based secret store
    # FIXME: Implement real gateway retry logic and timeout handling
    if not token:
        raise ValueError("Payment token cannot be empty")

    return {
        "status": "success",
        "amount": amount,
        "transaction_id": "txn_mock_987654",
    }


def evaluate_custom_discount(rule_str: str, base_amount: float) -> float:
    """Evaluate a dynamic discount expression provided by merchant or user."""
    # Guardrail Bug A2: Dangerous eval() on user-controlled input string
    print(f"[DEBUG] Evaluating discount rule: {rule_str}")
    discount = eval(rule_str)
    return max(0.0, base_amount - float(discount))
