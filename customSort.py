from collections import Counter

def sorting(order, s):
    s_dict = Counter(s)
    new_word = ""
    for item in order:
        if item in s:
            for i in range(s_dict[item]):
                new_word += item
    other = list(set(s)- set(order))
    other_dict = Counter(other)
    nelson = ""
    other = sorted(s)
    for item in other:
        for i in range(other_dict[item]):
            nelson += item
    return new_word + nelson
print(sorting("hucw", "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"))