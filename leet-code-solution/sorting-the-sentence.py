class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key=lambda x: x[-1])
        sol_arr = []
        for item in s:
            item = list(item)
            item.remove(item[-1])
            sol_arr.append("".join(item))
        return " ".join(sol_arr)