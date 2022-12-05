import pytest
from main import Item

def test_answer():
    item1 = Item("Phone", 100, 5)

    assert item1.calculate_total_price() == 500