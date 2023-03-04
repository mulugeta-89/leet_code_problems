import functools
def comparator(x, y):
    if x+y > y+x:
        return 1
    elif x+y < y+x:
        return -1
    else:
        return 0

def largestNumber(nums):
    nums = [str(num) for num in nums]
    nums.sort(key=functools.cmp_to_key(comparator), reverse=True)
    largest_num = "".join(nums)
    return "0" if largest_num[0] == "0" else largest_num
    
print(largestNumber([7,3,4,5]))
