from collections import Counter
def search(nums, target):
    if target not in nums:
        return [-1,-1]
    nums_dict = dict(Counter(nums))
    sol_arr = []
    if target in nums:
        sol_arr.append(nums.index(target))
    print(sol_arr)
    if nums_dict[target] >= 2:
        for i in range(nums_dict[target]-1):
            sol_arr.append(sol_arr[i])
        for i in range(nums_dict[target]):
            sol_arr[i] = sol_arr[i]+i
    if len(sol_arr) >= 2:
        return [sol_arr[0], sol_arr[-1]]
    return [sol_arr[0], sol_arr[0]]



print(search([3,3,3],3))