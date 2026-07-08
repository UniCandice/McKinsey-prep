"""01: Strings — classic HackerRank warm-ups.

Implement each function so the asserts at the bottom pass:
    python python/01_strings.py
"""


def reverse_string(s):
    """Return s reversed. 'hello' -> 'olleh'"""
    ...


def is_palindrome(s):
    """Case-insensitive, ignore spaces. 'Never odd or even' -> True"""
    ...


def count_vowels(s):
    """Number of vowels (aeiou, case-insensitive)."""
    ...


def first_non_repeating(s):
    """First character that appears exactly once, or None.
    'swiss' -> 'w'"""
    ...


def word_frequencies(text):
    """Dict of word -> count, lowercase, split on whitespace.
    'the cat the dog' -> {'the': 2, 'cat': 1, 'dog': 1}"""
    ...


def are_anagrams(a, b):
    """'listen', 'silent' -> True"""
    ...


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
    print("All string exercises pass ✔")
