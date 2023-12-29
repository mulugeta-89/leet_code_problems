class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_arr = []
        for item in nums1:
            while item in nums2:
                nums2.pop(nums2.index(item))
                new_arr.append(item)
                break
        return new_arr
