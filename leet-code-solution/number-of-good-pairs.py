class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dicti = Counter(nums)
        sol = 0
        for item in dicti:
            sol += (dicti[item] * (dicti[item]-1))/2
        return int(sol)

        