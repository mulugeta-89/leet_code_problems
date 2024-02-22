class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol_dict = {}
        sol_arr = []
        stack = []
        for item in nums2:
            while stack and stack[-1] < item:
                sol_dict[stack[-1]] = item
                stack.pop()
            stack.append(item)
        
        for k in nums1:
            if k not in sol_dict:
                sol_arr.append(-1)
            else:
                sol_arr.append(sol_dict[k])
        return sol_arr
        