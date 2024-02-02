class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        length = float("inf")
        sol_string = ""
        r_dict = Counter(t)
        s_dict = {}
        required = len(r_dict)
        finding_chars = 0

        for right in range(len(s)):
            s_dict[s[right]] = s_dict.get(s[right], 0) + 1

            if s_dict[s[right]] == r_dict[s[right]]:
                finding_chars += 1
            while finding_chars == required:
                if right-left+1 < length:
                    length = right-left+1
                    sol_string = s[left:right+1]
                s_dict[s[left]] -= 1
                if s_dict[s[left]] < r_dict[s[left]]:
                    finding_chars -= 1
                left += 1
        return sol_string