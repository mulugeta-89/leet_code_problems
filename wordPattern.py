def word_pattern(patt, s):
    new_patt = list(patt)
    new_a = s.split(" ")
    patt_dict ={}
    if len(new_patt) != len(new_a):
        return False
    for i in range(len(new_patt)):
        if new_patt[i]:
            patt_dict[new_patt[i]] = new_a[i]
    patt1 = list(patt_dict.keys())
    word = list(patt_dict.values())
    if len(set(patt1)) != len(set(word)):
        return False
    for i in range(len(new_patt)):
        run_dict = {}
        run_dict[new_patt[i]] = new_a[i]
        if run_dict[new_patt[i]] != patt_dict[new_patt[i]]:
            return False
    return True


print(word_pattern("abba", "dog dog dog dog"))
    