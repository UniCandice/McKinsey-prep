"""SOLUTIONS 01: Strings"""
from collections import Counter


def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    t = s.replace(" ", "").lower()
    return t == t[::-1]


def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")


def first_non_repeating(s):
    counts = Counter(s)
    for c in s:
        if counts[c] == 1:
            return c
    return None


def word_frequencies(text):
    return dict(Counter(text.lower().split()))


def are_anagrams(a, b):
    return sorted(a) == sorted(b)  # or Counter(a) == Counter(b)


if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert is_palindrome("Never odd or even") is True
    assert is_palindrome("hello") is False
    assert count_vowels("HackerRank") == 3
    assert first_non_repeating("swiss") == "w"
    assert first_non_repeating("aabb") is None
    assert word_frequencies("the cat the dog") == {"the": 2, "cat": 1, "dog": 1}
    assert are_anagrams("listen", "silent") is True
    assert are_anagrams("hello", "world") is False
    print("All string solutions pass ✔")
