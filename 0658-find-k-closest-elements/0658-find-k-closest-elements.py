class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        watcher = [i for i in range(len(arr))]
        l, r = 0, len(arr)-1
        while l != r:
            if abs(arr[l]-x) <= abs(arr[r]-x):
                r -= 1
            else:
                l += 1
            if watcher[r] - watcher[l] == k-1:
                return arr[l:r+1]
        return arr
        