import pytest
from calculator.operations import add, subtract, multiply, divide

#---------------------ADD TESTS (8) ---------------------
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_mixed():
    assert add(-2, 3) == 1

def test_add_zero():
    assert add(0, 5) == 5

def test_add_large():
    assert add(1000000, 2000000) == 3000000

def test_add_float():
    assert add(2.5, 2.5) == 5.0

def test_add_negative_positive():
    assert add(-10, 5) == -5

def test_add_zero_zero():
    assert add(0, 0) == 0

#--------------------SUBTRACT TESTS (7) ------------------
def test_subtract_positive():
    assert subtract(10, 5) == 5

def test_subtract_negative():
    assert subtract(-10, -5) == -5

def test_subtract_mixed():
    assert subtract(-10, 5) == -15

def test_subtract_zero():
    assert subtract(10, 0) == 10

def test_subtract_large():
    assert subtract(5000000, 2000000) == 3000000

def test_subtract_float():
    assert subtract(5.5, 2.5) == 3.0

def test_subtract_equal():
    assert subtract(5, 5) == 0

#---------------------MULTIPLY TESTS(7)
def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(-2, -3) == 6

def test_multiply_mixed():
    assert multiply(-2, 3) == -6

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_multiply_large():
    assert multiply(1000, 2000) == 2000000

def test_multiply_float():
    assert multiply(2.5, 2) == 5.0

def test_multiply_one():
    assert multiply(5, 1) == 5
#----------------DIVIDE TESTS(8)--------------
def test_divide_positive():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-10, -2) == 5
    
def test_divide_mixed():
    assert divide(-10, 2) == -5

def test_divide_float():
    assert divide(5, 2) == 2.5

def test_divide_one():
    assert divide(10, 1) == 10

def test_divide_large():
    assert divide(1000000, 1000) == 1000

def test_divide_zero_numerator():
    assert divide(0, 5) == 0

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)










    
