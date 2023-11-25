class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mini = float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                diff = abs(sums-target)
                if diff < mini:
                    sol = sums
                    mini = diff
                if sums > target:
                    k -= 1
                else:
                    j += 1
        return sol
        