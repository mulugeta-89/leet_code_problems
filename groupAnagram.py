from collections import Counter
def group(strs):
    strs_dict = {}
    for item in strs:
        item_string = ''.join(sorted(item))
        if item_string not in strs_dict:
            strs_dict[item_string] = [item]
        else:
            strs_dict[item_string].append(item)
    return list(strs_dict.values())


print(group(["eat","tea","tan","ate","nat","bat"]))