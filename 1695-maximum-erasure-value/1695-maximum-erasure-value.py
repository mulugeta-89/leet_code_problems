class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = {}
        left = 0
        sol = -1
        unique = 0
        curr_sum = 0
        for right in range(len(nums)):
            if nums[right] not in freq or freq[nums[right]] == 0:
                unique += 1
            curr_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while unique < right-left + 1:
                curr_sum -= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    unique -= 1
                left += 1
            sol = max(sol, curr_sum)
        return sol
        