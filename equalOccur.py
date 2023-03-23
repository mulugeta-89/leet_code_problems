from collections import Counter
def equal(s):
    some = Counter(s)
    if len(set(some.values())) == 1:
        return True
    return False
