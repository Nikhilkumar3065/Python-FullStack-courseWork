class Searching:
    def linear_search(self, arr, target):
        for index, value in enumerate(arr):
            if value == target:
                return index

        return -1
def binary_search(self, arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

    return -1