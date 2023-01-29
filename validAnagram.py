def validAnagram(s,t):
    if len(s)!= len(t):
        return False
    s_dict = {}
    for item in s:
        if item not in s_dict:
            s_dict[item] = 1
        else:
            s_dict[item] = s_dict[item]+1
    t_dict = {}
    for item in t:
        if item not in t_dict:
            t_dict[item] = 1
        else:
            t_dict[item] = t_dict[item]+1
    print(s_dict, t_dict)
    flag = False
    for item in s:
        if item not in t:
            flag = False
            break
        else:
            if s_dict[item] == t_dict[item]:
                flag =  True
    return flag
        

print(validAnagram("anagram", "nagaram"))