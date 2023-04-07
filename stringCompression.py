from itertools import groupby
def compression(chars):
    my_counts = [(elem, len(list(group))) for elem, group in groupby(chars)]
    chars.clear()
    for key, value in my_counts:
        if value == 1:
            chars.append(key)
        else:
            chars.append(key)
            chars += list(str(value))
    return len(chars)
print(compression(["a","a","a","b","b","a","a"]))

