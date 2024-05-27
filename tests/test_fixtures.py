import pytest
from utils.common import add, subtract

@pytest.fixture
def numbers():
    return 1, 2

def test_addition(numbers):
    a, b = numbers
    assert add(a, b) == 3

def test_subtraction(numbers):
    a, b = numbers
    assert subtract(a, b) == -1
