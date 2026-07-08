"""SOLUTIONS 03: Dictionaries"""
from collections import Counter, defaultdict


def char_frequency(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def top_n_frequent(words, n):
    return Counter(words).most_common(n)


def invert_dict(d):
    return {v: k for k, v in d.items()}


def merge_sum(d1, d2):
    out = dict(d1)
    for k, v in d2.items():
        out[k] = out.get(k, 0) + v
    return out


def group_by_first_letter(words):
    groups = defaultdict(list)
    for w in words:
        groups[w[0]].append(w)
    return dict(groups)


def total_spend_per_customer(transactions):
    totals = {}
    for cust, amount in transactions:
        totals[cust] = totals.get(cust, 0) + amount
    return totals


if __name__ == "__main__":
    assert char_frequency("aab") == {"a": 2, "b": 1}
    assert top_n_frequent(["a", "b", "a", "c", "a", "b"], 2) == [("a", 3), ("b", 2)]
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert merge_sum({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 5, "c": 4}
    assert group_by_first_letter(["apple", "avocado", "banana"]) == {
        "a": ["apple", "avocado"], "b": ["banana"]}
    assert total_spend_per_customer([(1, 10.0), (2, 5.0), (1, 2.5)]) == {1: 12.5, 2: 5.0}
    print("All dictionary solutions pass ✔")
