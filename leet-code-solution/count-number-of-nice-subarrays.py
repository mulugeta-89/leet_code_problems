class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sol = 0
        left = 0
        count = 0
        odd_indices = []
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                count += 1
                odd_indices.append(right)
            
            if count > k:
                left = odd_indices.pop(0) + 1
                count -= 1
            if count == k:
                sol += odd_indices[0]-left + 1
        return sol