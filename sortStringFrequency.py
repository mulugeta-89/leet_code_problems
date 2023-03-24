from collections import Counter

def sorting(s):
    some = dict(Counter(s))
    some = dict(sorted(some.items(), key=lambda x: (x[1]), reverse=True))
    sol_str = ""
    for key in some.keys():
        for i in range(some[key]):
            sol_str += key
    return sol_str
print(sorting("Aabb"))
