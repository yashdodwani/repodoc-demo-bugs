"""Tests for order processing and pricing calculations."""
import pytest
from app.orders import (
    get_recent_orders,
    calculate_discount,
    calculate_average_price,
    get_customer_name,
)


def test_get_recent_orders_limit():
    """Verify limit count is respected for recent orders.

    FAILS on Bug B4: Off-by-one slice orders[0:limit-1] returns 2 items instead of 3.
    """
    orders = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}]
    recent = get_recent_orders(orders, limit=3)
    assert len(recent) == 3
    assert [o["id"] for o in recent] == [1, 2, 3]


def test_get_recent_orders_empty():
    """Returns empty list when limit <= 0."""
    orders = [{"id": 1}, {"id": 2}]
    assert get_recent_orders(orders, limit=0) == []


def test_calculate_discount_percentage():
    """Verify standard 20% discount on $100 item equals $80.00.

    FAILS on Bug B5: Wrong operator (-) produces incorrect discount amount.
    """
    assert calculate_discount(100.0, 20.0) == 80.0


def test_calculate_average_price_populated():
    """Average price calculation with populated item list passes."""
    items = [{"price": 10.0}, {"price": 20.0}, {"price": 30.0}]
    assert calculate_average_price(items) == 20.0


def test_calculate_average_price_empty_list():
    """Calculate average price of empty item list should return 0.0 without crashing.

    FAILS on Bug B6: ZeroDivisionError on len(items) == 0.
    """
    assert calculate_average_price([]) == 0.0


def test_get_customer_name_valid():
    """Retrieves customer name from valid order dict."""
    order = {"id": 101, "customer": {"name": "Alice Walker"}}
    assert get_customer_name(order) == "Alice Walker"
