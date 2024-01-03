class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start = 0
        tot = 0
        end = len(skill)-1
        should = skill[start] + skill[end]
        while start < end:
            if skill[start] + skill[end] != should:
                return -1
            else:
                tot += (skill[start]*skill[end])
                start += 1
                end -= 1
        return tot
        