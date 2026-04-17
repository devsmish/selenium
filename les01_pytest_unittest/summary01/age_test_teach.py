import pytest
from age import AgeValidator

@pytest.fixture
def validator():
    return AgeValidator()

def test_is_adult_with_age_18(validator):
    assert validator.is_adult(18) is True

def test_is_adult_with_age_above_18(validator):
    assert validator.is_adult(25) is True

def test_is_adult_with_age_below_18(validator):
    assert validator.is_adult(17) is False

def test_is_adult_with_zero(validator):
    assert validator.is_adult(0) is False

def test_is_adult_with_negative_age(validator):
    assert validator.is_adult(-5) is False

def test_is_adult_with_float_age(validator):
    assert validator.is_adult(18.5) is True
    assert validator.is_adult(17.9) is False
