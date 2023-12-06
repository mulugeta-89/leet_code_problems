class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sol_arr = [" " for i in s]
        for i in range(len(s)):
            sol_arr[indices[i]] = s[i]
        return "".join(sol_arr)