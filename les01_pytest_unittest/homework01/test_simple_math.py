from les01_pytest_unittest.homework01.simple_math import SimpleMath
import pytest

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_square_pos(simple_math):
    assert simple_math.square(2) == 4

def test_square_null(simple_math):
    assert simple_math.square(0) == 0

def test_square_neg(simple_math):
    assert simple_math.square(-2) == 4

def test_cube_pos(simple_math):
    assert simple_math.cube(2) == 8

def test_cube_null(simple_math):
    assert simple_math.cube(0) == 0

def test_cube_neg(simple_math):
    assert simple_math.cube(-2) == -8
