def sumAbsoluteDifference(nums):
    sumi = 0
    sol_arr = []
    prefix_sum = [0] * len(nums)
    suffix_sum = [0] * len(nums)
    for i in range(len(nums)):
        prefix_sum[i] = sumi
        sumi += nums[i]
    sumi = 0
    for j in range(len(nums)-1, -1, -1):
        suffix_sum[j] = sumi
        sumi += nums[j]
    for i in range(len(nums)):
        lower_sum = abs(prefix_sum[i] - (nums[i]*i))
        upper_sum = abs((len(nums)-i-1) * nums[i] - (suffix_sum[i]))
        sol_arr.append(lower_sum+upper_sum)
    return sol_arr
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        nums_dict = defaultdict(list)
        container = []
        sol_arr = [0] * len(nums)
        for ind, item in enumerate(nums):
            nums_dict[item].append(ind)
        for key in nums_dict:
            diff = sumAbsoluteDifference(nums_dict[key])
            container.append((nums_dict[key], diff))
        for a,b in container:
            for i in range(len(a)):
                sol_arr[a[i]] = b[i]
        return sol_arr