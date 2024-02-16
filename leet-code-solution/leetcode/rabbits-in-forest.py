class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        arr = []
        ans = dict(Counter(answers))
        for k in ans:
            min_group = math.ceil(ans[k]/(k+1))
            arr.append((k, min_group))
        sol = 0
        for item in arr:
            sol += ((item[0]+1)*item[1])
        return sol
        