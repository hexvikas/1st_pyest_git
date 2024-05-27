import pytest

@pytest.mark.parametrize("a, b, result", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 10, 20)
])
def test_add(a, b, result):
    assert a + b == result
