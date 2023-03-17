def counting_prefix(words, pref):
    answer = 0
    len_pref = len(pref)
    for item in words:
        new_string = item[:len_pref]
        if new_string == pref:
            answer += 1
    return answer
print(counting_prefix(["leetcode","win","loops","success"], "code"))
