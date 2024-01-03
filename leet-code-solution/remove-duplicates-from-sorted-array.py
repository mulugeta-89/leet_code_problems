class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[count] = nums[i]
                count = count + 1
                prev = nums[i]
        return count