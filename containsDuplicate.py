
def containsDuplicate(self, nums: List[int]) -> bool:
    nums_dict = {}
    for item in nums:
        if item not in nums_dict:
            nums_dict[item] = 1
        else:
            nums_dict[item] = nums_dict[item]+1
    for key in nums_dict.keys():
        if nums_dict[key] >1:
            return True
    return False