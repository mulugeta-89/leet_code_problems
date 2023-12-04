class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        len_array = [len(item) for item in s]
        maxi_length = max(len_array)
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
        