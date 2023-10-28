class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        dicto = {}
        for i in range(len(nums)):
            if nums[i] == target:
                diff = abs(i-start)
                dicto[i] = diff
            diff = 0
        dicto = dict(sorted(dicto.items(), key=lambda x: x[1]))
        for key in dicto.keys():
            return dicto[key]
        