def longest(s):
    if s=="":
        return 0
    running = ""
    maxi = 1
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[j] in running:
                maxi = max(maxi, len(running))
                running = ""
            running += s[j]
            maxi = max(maxi, len(running))
        running = ""
    return maxi
print(longest("asjrgapa"))