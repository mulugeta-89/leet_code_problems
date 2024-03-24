class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        pivot = l
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            mid_val = nums[(mid+pivot)%len(nums)]

            if mid_val == target:
                return (mid+pivot) % len(nums)
            elif target < mid_val:
                right = mid -1
            else:
                left = mid + 1
        return -1
        