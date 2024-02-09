class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum =[0] * (len(s)-1)
        suffix_sum = [0] * (len(s)-1)
        count = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                count += 1
            prefix_sum[i] += count
        count1 = 0
        for i in range(len(s)-1, 0, -1):
            if s[i] == "1":
                count1 += 1
            suffix_sum[i-1] += count1
        maxi = -1
        for i in range(len(suffix_sum)):
            sumi = suffix_sum[i]+prefix_sum[i]
            maxi = max(maxi, sumi)
        return maxi