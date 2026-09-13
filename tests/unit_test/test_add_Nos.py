import pytest
from src.add_nos import add_nos


@pytest.mark.unit
def test_add_nos():
    result = add_nos(29, 30)
    assert result == 59
