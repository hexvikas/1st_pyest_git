import pytest

@pytest.mark.smoke
def test_smoke_example():
    assert 1 == 1

@pytest.mark.regression
def test_regression_example():
    assert 2 == 2
