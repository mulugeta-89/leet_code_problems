class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sol = []
        for i in range(len(arr)-1, 0, -1):
            maxi = max(arr[:i+1])
            ind = arr.index(maxi)

            if ind != i:
                arr[:ind+1] = arr[:ind+1][::-1]
                sol.append(ind+1)

                arr[:i+1] = arr[:i+1][::-1]
                sol.append(i+1)
        return sol