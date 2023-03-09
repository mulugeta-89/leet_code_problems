def occur(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1
print(occur("leetcode","leeto"))