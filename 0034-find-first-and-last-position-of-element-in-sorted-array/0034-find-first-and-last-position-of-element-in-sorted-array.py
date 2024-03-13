class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= target:
                high = mid-1
            else:
                low = mid+1
        left, right = low, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                left = mid+1
            else:
                right = mid-1
        return [low, right]

        