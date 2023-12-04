class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        maxi_length = -1
        for item in s:
            if len(item) > maxi_length:
                maxi_length = len(item)
        for i in range(len(s)):
            if len(s[i]) < maxi_length:
                s[i] += " " * (maxi_length-len(s[i]))
        sol_arr = []
        for i in range(maxi_length):
            temp = ""
            for item in s:
                temp += item[i]
            sol_arr.append(temp)
        return list(map(lambda word: word.rstrip(), sol_arr))
        