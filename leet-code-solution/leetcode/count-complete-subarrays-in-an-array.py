class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        count = 0
        for i in range(len(nums)):
            container = set()
            for j in range(i, len(nums)):
                container.add(nums[j])
                if n == len(container):
                    count += 1
        return count
        