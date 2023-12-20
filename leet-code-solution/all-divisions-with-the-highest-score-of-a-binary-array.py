class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        maxi = max(prefix)
        soli = maxi
        sol_arr = []
        for i in range(len(nums)):
            j = i+1
            temp = abs(j-prefix[i]) + (maxi - prefix[i])
            if temp > soli:
                soli = temp
                sol_arr = [j]
            elif temp == soli:
                sol_arr.append(j)
        if soli == max(prefix):
            sol_arr.append(0)
        return sol_arr
        