class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi = 0
        for trip in trips:
            maxi = max(maxi, trip[-1])
        arr = [0] * (maxi+1)
        for p,f,t in trips:
            arr[f] += p
            if t < maxi:
                arr[t] -= p
        for i in range(1, len(arr)):
            arr[i] = arr[i-1] + arr[i]
        if max(arr) <= capacity:
            return True
        return False