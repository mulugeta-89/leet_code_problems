class Solution:
    def searchInsert(self, arr: List[int], k: int) -> int:
        if k in arr:
            return arr.index(k)
        arr.append(k)
        arr = sorted(arr)
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                right = mid -1
            else:
                left = mid + 1