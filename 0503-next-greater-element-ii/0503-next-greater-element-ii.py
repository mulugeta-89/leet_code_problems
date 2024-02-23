class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        dicti = {}
        for ind,val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                dicti[stack[-1]] = val
                stack.pop()
            stack.append(ind)
        for ind,val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                dicti[stack[-1]] = val
                stack.pop()
            stack.append(ind)
        sol_arr = []
        for i in range(len(nums)):
            if i in dicti:
                sol_arr.append(dicti[i])
            else:
                sol_arr.append(-1)
        return sol_arr
        