class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l,r = 0, 0
        while r < len(typed):
            if l < len(name) and name[l] == typed[r]:
                l += 1
                r += 1
            elif r > 0 and typed[r-1] == typed[r]:
                r += 1
            else:
                return False
        return l == len(name)
        