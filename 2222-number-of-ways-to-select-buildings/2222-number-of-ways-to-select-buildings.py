class Solution:
    def numberOfWays(self, s: str) -> int:
        num_zeros = [0] * len(s)
        num_ones = [0] * len(s)
        count_zero = 0
        count_one = 0
        for i in range(len(s)):
            num_ones[i] = count_one
            num_zeros[i] = count_zero
            if s[i] == "0":
                count_zero += 1
            if s[i] == "1":
                count_one += 1
        num_ol = [0] * len(s)
        num_lo = [0] * len(s)
        for i in range(1,len(s)):
            if s[i] == "1":
                num_lo[i] = num_lo[i-1]
                num_ol[i] = num_ol[i-1] + num_zeros[i]
            elif s[i]:
                num_lo[i] = num_lo[i-1] + num_ones[i]
                num_ol[i] = num_ol[i-1]
        num_olo = [0] * len(s)
        num_lol = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == "1":
                num_olo[i] = num_olo[i-1]
                num_lol[i] = num_lol[i-1] + num_lo[i]
            else:
                num_olo[i] = num_olo[i-1] + num_ol[i]
                num_lol[i] = num_lol[i-1]
        return num_olo[-1] + num_lol[-1]
        