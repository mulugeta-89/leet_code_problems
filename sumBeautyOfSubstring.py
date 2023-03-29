from collections import Counter

def beautySum(s):
    total = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            maxi = 0
            mini = 0
            some_arr = s[i:j+1]
            if len(set(some_arr)) == 1:
                continue
            else:
                some_dict = Counter(some_arr)
                maxi = max(list(some_dict.values()))
                mini = min(list(some_dict.values()))
                total += (maxi-mini)
    return total
print(beautySum("aabcbaa"))
