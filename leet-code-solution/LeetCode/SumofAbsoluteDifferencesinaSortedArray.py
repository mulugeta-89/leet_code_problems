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
            lower_sum = (nums[i]*i) - prefix_sum[i]
            upper_sum = (suffix_sum[i]) - (len(nums)-i-1) * nums[i]
            sol_arr.append(lower_sum+upper_sum)
        return sol_arr