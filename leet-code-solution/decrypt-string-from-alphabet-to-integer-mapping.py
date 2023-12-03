class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alpha_dict = {str(id+1):char for id,char in enumerate(alphabet)}
        sol = ""
        end = len(s)-1
        while end >= 0:
            if s[end] == "#":
                temp = end
                end -= 3
                item = s[end+1:temp]
                sol += alpha_dict[item]
            else:
                sol += alpha_dict[s[end]]
                end -= 1
        return sol[::-1]
        