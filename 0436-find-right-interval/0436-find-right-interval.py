class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sol_arr = [0] * n
        for i, interval in enumerate(intervals):
            interval.append(i)
        intervals.sort()
        for i, interval in enumerate(intervals):
            a,b,c = interval
            ans = float("inf")
            l, r = i, n-1
            while l <= r:
                mid = (l+r)//2
                i,j,k = intervals[mid]
                if b <= i:
                    ans = min(ans, i)
                    r = mid-1
                else:
                    l = mid+1
            sol_arr[c] = intervals[l][2] if ans != float("inf") else -1
        return sol_arr