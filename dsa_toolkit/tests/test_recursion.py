from dsa.recursion import Recursion
def test_factorial():
    r = Recursion()
    assert r.factorial(5) == 120
def test_reverse_string():
    r = Recursion()
    assert r.reverse_string("abc") == "cba"