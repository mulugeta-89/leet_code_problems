class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        sol = []
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == 0:
                    if [nums[i], nums[j], nums[k]] not in sol:
                        sol.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif sums > 0:
                    k -= 1
                else:
                    j += 1
        return sol