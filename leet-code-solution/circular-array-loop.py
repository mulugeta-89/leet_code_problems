class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        for i in range(len(nums)):
            if i not in visited:
                small = set()
                while True:
                    if i in small:
                        return True
                    
                    visited.add(i)
                    small.add(i)
                    prev, i = i, (i + nums[i])%len(nums)
                    if prev == i or (nums[i] >0) != (nums[prev] > 0):
                        break
        return False
        