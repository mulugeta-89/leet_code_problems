class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_set = set(s)
        last_index = {}
        container = set()
        for i in range(len(s)):
            last_index[s[i]] = i
        maxi = 0
        sol_arr = []
        pointer = 0
        for i in range(len(s)):
            end_index = last_index[s[i]]
            maxi = max(maxi, end_index)
            if i == maxi:
                length = end_index-pointer + 1
                sol_arr.append(length)
                pointer += length
        return sol_arr
        