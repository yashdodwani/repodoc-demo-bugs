"""Tests for utility helpers and shopping cart operations."""
import pytest
from app.utils import add_item_to_cart, format_currency, chunk_list


def test_add_item_independent_carts():
    """Cart default argument must not retain state across consecutive calls.

    FAILS on Bug B8: Mutable default argument cart=[] causes second call
    to contain items from first call.
    """
    cart1 = add_item_to_cart("laptop")
    assert cart1 == ["laptop"]

    cart2 = add_item_to_cart("mouse")
    # Due to mutable default argument, cart2 is ["laptop", "mouse"] instead of ["mouse"]
    assert cart2 == ["mouse"]


def test_format_currency():
    """Formats float value into standard currency string."""
    assert format_currency(1234.5) == "$1,234.50"
    assert format_currency(0.0) == "$0.00"


def test_chunk_list():
    """Chunks list into evenly sized sublists."""
    data = ["a", "b", "c", "d", "e"]
    assert chunk_list(data, 2) == [["a", "b"], ["c", "d"], ["e"]]
