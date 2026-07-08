"""04: Simple algorithms — the level HackerRank easy/medium actually asks.

Implement each function so the asserts pass:
    python python/04_algorithms.py
"""


def fizzbuzz(n):
    """List of 1..n with multiples of 3 -> 'Fizz', 5 -> 'Buzz',
    both -> 'FizzBuzz' (as strings; plain numbers stay ints)."""
    ...


def two_sum(nums, target):
    """Indices of the two numbers adding to target (one solution
    guaranteed). [2,7,11,15], 9 -> (0, 1). Aim for O(n) with a dict."""
    ...


def fibonacci(n):
    """First n Fibonacci numbers. 5 -> [0, 1, 1, 2, 3]"""
    ...


def is_prime(n):
    """True if n is prime. Only test divisors up to sqrt(n)."""
    ...


def binary_search(sorted_nums, target):
    """Index of target in a sorted list, or -1."""
    ...


def max_subarray_sum(nums):
    """Largest sum of a contiguous subarray (Kadane's).
    [-2,1,-3,4,-1,2,1,-5,4] -> 6"""
    ...


def missing_number(nums):
    """nums contains 0..n with exactly one number missing.
    [3,0,1] -> 2 (sum formula or XOR)"""
    ...


if __name__ == "__main__":
    assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert is_prime(97) is True and is_prime(1) is False and is_prime(4) is False
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5], 4) == -1
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert missing_number([3, 0, 1]) == 2
    print("All algorithm exercises pass ✔")
