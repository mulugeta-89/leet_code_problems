def isSubsequence(s, r):
    i,j = 0,0
    while i < len(r) and j < len(s):
        if r[i] == s[j]:
            i += 1
        j += 1
    return i == len(r)
def findLongest(s, dictionary):
    sol_arr = []
    maxi = 0
    for item in dictionary:
        res = isSubsequence(s, item)
        if res:
            maxi = max(maxi, len(item))
            sol_arr.append(item)
    if len(sol_arr) > 1:
        sol_arr = list(filter(lambda x: len(x) == maxi, sol_arr))
        sol = sol_arr[0]
        for i in range(1, len(sol_arr)):
            if sol_arr[i] < sol:
                sol = sol_arr[i]
        return sol
    return sol_arr[0] if len(sol_arr) == 1 else ""
print(findLongest("apple",["xx","io"]))
