class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        all = set(fronts).union(set(backs))
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in all:
                all.remove(fronts[i])
        if len(all) == 0:
            return 0
        return all.pop()
        