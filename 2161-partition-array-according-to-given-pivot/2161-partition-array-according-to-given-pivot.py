class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [item for item in nums if item < pivot]
        equal = [item for item in nums if item == pivot]
        greater = [item for item in nums if item > pivot]
        return less + equal + greater
        