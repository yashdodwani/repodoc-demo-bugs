"""Common utility functions and data manipulation helpers."""
from typing import List, Optional


def add_item_to_cart(item: str, cart: List[str] = []) -> List[str]:
    """Append an item to a customer shopping cart.

    Logic Bug B8: Mutable default argument cart=[] persists across invocations.
    """
    # FIXME: Avoid mutable default argument, use cart: Optional[List[str]] = None
    cart.append(item)
    return cart


def format_currency(amount: float) -> str:
    """Format numeric float into USD currency representation."""
    return f"${amount:,.2f}"


def chunk_list(items: List[str], chunk_size: int) -> List[List[str]]:
    """Partition a list into sublists of size `chunk_size`."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]
