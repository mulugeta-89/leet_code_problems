class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        sol_arr = [0] * (n+1)
        for a,b,k in bookings:
            sol_arr[a-1] += k
            sol_arr[b] -= k
        for i in range(1, len(sol_arr)):
            sol_arr[i] = sol_arr[i-1] + sol_arr[i]
        return sol_arr[:len(sol_arr)-1]
        