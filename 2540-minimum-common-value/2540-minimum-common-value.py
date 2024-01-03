class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)
        for k in nums1_dict:
            if k in nums2_dict:
                return k
        return -1
        