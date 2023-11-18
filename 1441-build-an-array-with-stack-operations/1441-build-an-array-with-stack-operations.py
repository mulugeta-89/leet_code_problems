class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        sol = []
        copier = []
        k = 0
        for i in range(1, n+1):
            if i == target[k]:
                sol.append("Push")
                copier.append(i)
                k += 1
                if copier == target:
                    break
                continue
            elif len(sol) == 0 and i != target[k]:
                sol.append("Push")
                sol.append("Pop")
                continue
            elif i != target[k]:
                sol.append("Push")
                sol.append("Pop")
        return sol