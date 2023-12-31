class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sol_arr = []
        for item in nums:
            count = 0
            for i in range(len(nums)):
                if nums[i] < item:
                    count += 1
            sol_arr.append(count)
        return sol_arr





            
                

        