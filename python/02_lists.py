"""02: Lists & comprehensions.

Implement each function so the asserts pass:
    python python/02_lists.py
"""


def squares_of_evens(nums):
    """One list comprehension: squares of the even numbers.
    [1,2,3,4] -> [4,16]"""
    ...


def second_largest(nums):
    """Second-largest UNIQUE value. [5,5,4,1] -> 4"""
    ...


def flatten(nested):
    """One level: [[1,2],[3],[4,5]] -> [1,2,3,4,5]"""
    ...


def running_sum(nums):
    """[1,2,3,4] -> [1,3,6,10]"""
    ...


def chunk(nums, size):
    """[1,2,3,4,5], 2 -> [[1,2],[3,4],[5]]"""
    ...


def moving_average(nums, window):
    """[1,2,3,4,5], 3 -> [2.0, 3.0, 4.0]"""
    ...


def sort_by_length_then_alpha(words):
    """Sort by length, ties alphabetical.
    ['bb','a','ccc','aa'] -> ['a','aa','bb','ccc']"""
    ...


if __name__ == "__main__":
    assert squares_of_evens([1, 2, 3, 4]) == [4, 16]
    assert second_largest([5, 5, 4, 1]) == 4
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]
    assert sort_by_length_then_alpha(["bb", "a", "ccc", "aa"]) == ["a", "aa", "bb", "ccc"]
    print("All list exercises pass ✔")
