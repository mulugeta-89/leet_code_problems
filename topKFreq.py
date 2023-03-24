from collections import Counter

def frequent(words, k):
    words_dict = dict(Counter(words))
    words_dict = dict(sorted(words_dict.items(), key=lambda x: (-x[1], x[0])))
    return list(words_dict.keys())[:k]
print(frequent(["i","love","leetcode","i","love","coding", "a", "a"], 3))
