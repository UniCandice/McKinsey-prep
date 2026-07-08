"""03: Dictionaries — the d.get(k, 0) + 1 pattern and friends.

Implement each function so the asserts pass:
    python python/03_dictionaries.py
"""


def char_frequency(s):
    """Manual counting with .get() — no Counter.
    'aab' -> {'a': 2, 'b': 1}"""
    ...


def top_n_frequent(words, n):
    """N most frequent words as [(word, count)], most frequent first.
    Use collections.Counter and .most_common()."""
    ...


def invert_dict(d):
    """{'a': 1, 'b': 2} -> {1: 'a', 2: 'b'} (assume unique values)"""
    ...


def merge_sum(d1, d2):
    """Merge, summing values for shared keys.
    {'a':1,'b':2}, {'b':3,'c':4} -> {'a':1,'b':5,'c':4}"""
    ...


def group_by_first_letter(words):
    """['apple','avocado','banana'] ->
    {'a': ['apple','avocado'], 'b': ['banana']}
    (Try collections.defaultdict(list))"""
    ...


def total_spend_per_customer(transactions):
    """transactions: list of (customer_id, amount) tuples.
    [(1, 10.0), (2, 5.0), (1, 2.5)] -> {1: 12.5, 2: 5.0}"""
    ...


if __name__ == "__main__":
    assert char_frequency("aab") == {"a": 2, "b": 1}
    assert top_n_frequent(["a", "b", "a", "c", "a", "b"], 2) == [("a", 3), ("b", 2)]
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert merge_sum({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 5, "c": 4}
    assert group_by_first_letter(["apple", "avocado", "banana"]) == {
        "a": ["apple", "avocado"], "b": ["banana"]}
    assert total_spend_per_customer([(1, 10.0), (2, 5.0), (1, 2.5)]) == {1: 12.5, 2: 5.0}
    print("All dictionary exercises pass ✔")
