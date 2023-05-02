
def arraySign(self, nums: List[int]) -> int:
    if 0 in nums:
        return 0
    count = 0
    for item in nums:
        if item < 0:
            count+=1
    if count %2 == 0:
        return 1
    return -1