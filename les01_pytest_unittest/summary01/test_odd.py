import pytest
from les01_pytest_unittest.summary01.odd import EvenOddChecker

@pytest.fixture
def odd_checker():
    return EvenOddChecker()

def test_odd(odd_checker):
    assert odd_checker.is_odd(2) == False
    assert odd_checker.is_odd(3) == True
    assert odd_checker.is_odd(-2) == False

def test_even(odd_checker):
    assert odd_checker.is_even(2) == True
    assert odd_checker.is_even(3) == False
    assert odd_checker.is_even(-2) == True