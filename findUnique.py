def unique(s):
    s = str(s)
    s_dict = {}
    if not s:
        return -1
    for item in s:
        if item not in s_dict:
            s_dict[item] = 1
        else:
            s_dict[item] = s_dict[item] + 1
    if 1 not in s_dict.values():
        return -1
    for key in s_dict.keys():
        if s_dict[key] == 1:
            return s.index(key)
print(unique("leetcode"))