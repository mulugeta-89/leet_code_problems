
def findDuplicate(self, nums: List[int]) -> int:
    nums_dict = Counter(nums)
    nums_dict = dict(sorted(nums_dict.items(),key=lambda x: x[1],reverse=True))
    for key in nums_dict.keys():
        if nums_dict[key] > 1:
            return key