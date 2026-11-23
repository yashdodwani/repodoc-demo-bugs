"""Order processing and pricing calculations."""
from typing import List, Dict, Any


def get_recent_orders(
    orders: List[Dict[str, Any]], limit: int) -> List[Dict[str, Any]]:
    """Return the first `limit` recent orders.

    Logic Bug B4: Off-by-one slice error. Returns `limit - 1` items instead of `limit`.
    """
    # TODO: Support cursor-based pagination
    if limit <= 0:
        return []
    return orders[0 : limit - 1]  # Off-by-one: should be orders[0:limit]


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discounted price given a percentage discount (0-100).

    Logic Bug B5: Wrong operator in discount calculation.
    Uses `-` instead of `*` when computing discount amount.
    """
    # Bug: price - (discount_percent / 100.0) instead of price * (discount_percent / 100.0)
    discount_amount = price - (discount_percent / 100.0)
    final_price = price - discount_amount
    return round(final_price, 2)


def calculate_average_price(items: List[Dict[str, Any]]) -> float:
    """Calculate average price of items in order.

    Logic Bug B6: ZeroDivisionError when item list is empty.
    """
    # FIXME: Handle empty item list gracefully
    total = sum(item["price"] for item in items)
    return total / len(items)  # Raises ZeroDivisionError if items is empty


def get_customer_name(order: Dict[str, Any]) -> str:
    """Retrieve formatted customer name from an order dictionary.

    Logic Bug B10: Missing None check. Raises AttributeError when 'customer' is None.
    """
    customer_info = order.get("customer")
    # Bug: If order['customer'] is None, customer_info.get raises AttributeError
    return customer_info.get("name", "Unknown").strip()
