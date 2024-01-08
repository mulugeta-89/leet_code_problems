class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        sol = []
        for i in range(len(nums)-2):
            if i==0 or nums[i-1] != nums[i]:
                j = i+1
                k = len(nums)-1
                while j < k:
                    sums = nums[i] + nums[j] + nums[k]
                    if sums == 0:
                        sol.append([nums[i], nums[j], nums[k]])
                        while j <k and nums[j] == nums[j+1]: j+=1
                        while j < k and nums[k] == nums[k-1]: k -= 1
                        j += 1
                        k -= 1
                    elif sums > 0:
                        k -= 1
                    else:
                        j += 1
        return sol