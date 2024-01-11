class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        color_dict = {"W":0,"B":0}
        left = 0
        for i in range(k):
            color_dict[blocks[i]] += 1
        sol = color_dict["W"]
        for right in range(k, len(blocks)):
            color_dict[blocks[right]] += 1
            while right-left+1 > k:
                color_dict[blocks[left]] -= 1
                left += 1
            sol = min(sol, color_dict["W"])
        return sol
        