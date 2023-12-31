class Solution:
    def smallestNumber(self, nums: int) -> int:
        if nums == 0:
            return 0
        if nums >= 0:
            nums = str(nums)
            nums = [char for char in nums]
            nums.sort()
            if nums[0] == "0":
                i = 0
                while True:
                    i += 1
                    if nums[i] != "0":
                        nums[0], nums[i] = nums[i], nums[0]
                        break
            nums = "".join(nums)
            return int(nums)
        else:
            nums = str(nums)
            nums = [char for char in nums]
            nums.sort(reverse=True)
            nums.remove(nums[-1])
            nums = "".join(nums)
            return 0-int(nums)
        