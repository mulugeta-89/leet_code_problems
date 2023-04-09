from collections import Counter

def original(changed):
    if len(changed) % 2 != 0:
        return []
    changed_dict =Counter(changed)
    sol_arr = []
    for k in sorted(changed_dict):
        value = k*2
        while changed_dict[k] > 0:
            if changed_dict[value] == 0:
                return []
            sol_arr.append(k)
            changed_dict[k] -= 1
            changed_dict[value] -= 1
    return sol_arr
print(original([1,2,3,4,6,8]))
