from dsa.searching import Searching
def test_linear_search():
    s = Searching()
    assert s.linear_search([1, 2, 3], 2) == 1