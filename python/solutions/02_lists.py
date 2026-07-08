"""SOLUTIONS 02: Lists & comprehensions"""


def squares_of_evens(nums):
    return [x * x for x in nums if x % 2 == 0]


def second_largest(nums):
    return sorted(set(nums))[-2]


def flatten(nested):
    return [x for sub in nested for x in sub]


def running_sum(nums):
    out, total = [], 0
    for x in nums:
        total += x
        out.append(total)
    return out


def chunk(nums, size):
    return [nums[i:i + size] for i in range(0, len(nums), size)]


def moving_average(nums, window):
    return [sum(nums[i:i + window]) / window
            for i in range(len(nums) - window + 1)]


def sort_by_length_then_alpha(words):
    return sorted(words, key=lambda w: (len(w), w))


if __name__ == "__main__":
    assert squares_of_evens([1, 2, 3, 4]) == [4, 16]
    assert second_largest([5, 5, 4, 1]) == 4
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]
    assert sort_by_length_then_alpha(["bb", "a", "ccc", "aa"]) == ["a", "aa", "bb", "ccc"]
    print("All list solutions pass ✔")
