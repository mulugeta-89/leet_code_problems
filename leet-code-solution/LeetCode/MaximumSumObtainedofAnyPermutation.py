class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        nums.sort()
        arr = [0] * len(nums)
        for a,b in requests:
            arr[a] += 1
            if b+1 < len(nums):
                arr[b+1] -= 1
        for i in range(1, len(arr)):
            arr[i] = arr[i-1] + arr[i]
        arr.sort()
        sol = 0
        for i in range(len(arr)):
            sol += (arr[i]*nums[i])
        return sol% mod