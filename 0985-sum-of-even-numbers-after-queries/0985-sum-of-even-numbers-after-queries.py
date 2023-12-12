class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumofeven = 0
        for item in nums:
            if item %2 == 0:
                sumofeven += item
        sol_arr = []
        for val, ind in queries:
            if nums[ind] %2 == 0:
                sumofeven -= nums[ind]
            nums[ind] += val
            if nums[ind] % 2 == 0:
                sumofeven += nums[ind]
            sol_arr.append(sumofeven)
        return sol_arr
        