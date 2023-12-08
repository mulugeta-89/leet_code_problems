class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        sol_arr = []
        for i in range(n):
            sol_arr.append(nums[i])
            sol_arr.append(nums[i+n])
        return  sol_arr
        