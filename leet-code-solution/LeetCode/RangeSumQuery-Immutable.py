class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        sol  = 0
        for i in range(left, right+1):
            sol += self.nums[i]
        return sol