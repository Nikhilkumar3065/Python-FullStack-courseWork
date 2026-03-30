from dsa.sorting import Sorting
def test_bubble_sort():
    s = Sorting()
    assert s.bubble_sort([3, 1, 2]) == [1, 2, 3]