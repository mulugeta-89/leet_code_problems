class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        pos, n = 0, len(arr)
        while pos < n-1 and arr[pos] < arr[pos+1]:
            pos += 1
        if pos == 0 or pos == n-1:
            return False
        while pos < n-1 and arr[pos] > arr[pos+1]:
            pos += 1
        if pos == n-1:
            return True
        else:
            return False
        