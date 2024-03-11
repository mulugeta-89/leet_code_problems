class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        maxi = -1
        sol = ""
        for i in range(len(s)):
            temp = s[i]
            for j in range(i+1, len(s)):
                temp += s[j]
                flag = True
                for k in temp:
                    small = ""
                    if k.isupper():
                        small = k.lower()
                    if k.islower():
                        small = k.upper()
                    if small not in temp:
                        flag = False
                if flag and len(temp) > maxi:
                    maxi = len(temp)
                    sol = temp
        return sol

                
                    


        