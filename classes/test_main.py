import pytest
from main import Item

def test_should_return_total_price():
    item1 = Item("Phone", 100, 5)
    expected = 500
    actual = item1.calculate_total_price()
    assert actual == expected