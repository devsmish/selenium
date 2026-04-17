import pytest
from les01_pytest_unittest.summary01.age import AgeValidator

@pytest.fixture
def age_checker():
    return AgeValidator()

def test_age_invalid(age_checker):
    assert age_checker.is_adult(0) is False
    assert age_checker.is_adult(17) is False

def test_age_valid(age_checker):
    assert age_checker.is_adult(18) is True
    assert age_checker.is_adult(19) is True
    assert age_checker.is_adult(100) is True
