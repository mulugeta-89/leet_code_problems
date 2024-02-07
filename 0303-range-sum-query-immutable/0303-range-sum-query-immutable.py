class NumArray:

    def __init__(self, nums: List[int]):
        arr = [0] * len(nums)
        arr[0] = nums[0]
        for i in range(1, len(nums)):
            arr[i] = arr[i-1] + nums[i]
        
        self.nums = arr
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)