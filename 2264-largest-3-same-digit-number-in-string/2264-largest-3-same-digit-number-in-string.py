class Solution:
    def largestGoodInteger(self, num: str) -> str:
        sol = []
        for i in range(len(num)-2):
            if len(set(num[i: i+3])) == 1:
                sol.append(num[i:i+3])
        sol = sorted(sol, key=lambda x: int(x), reverse=True)
        return sol[0] if len(sol) >0 else ""
        