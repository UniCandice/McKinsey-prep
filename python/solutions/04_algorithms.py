"""SOLUTIONS 04: Simple algorithms"""


def fizzbuzz(n):
    return ["FizzBuzz" if i % 15 == 0 else
            "Fizz" if i % 3 == 0 else
            "Buzz" if i % 5 == 0 else i
            for i in range(1, n + 1)]


def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], i)
        seen[x] = i


def fibonacci(n):
    out, a, b = [], 0, 1
    for _ in range(n):
        out.append(a)
        a, b = b, a + b
    return out


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def binary_search(sorted_nums, target):
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == target:
            return mid
        if sorted_nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def max_subarray_sum(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert is_prime(97) is True and is_prime(1) is False and is_prime(4) is False
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5], 4) == -1
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert missing_number([3, 0, 1]) == 2
    print("All algorithm solutions pass ✔")
