
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        s_dict = {}
        p_dict = {}

        for i in range(len(p)):
            p_dict[p[i]] = p_dict.get(p[i], 0) + 1
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1

        sol_arr = [0] if p_dict == s_dict else []

        left = 0
        for right in range(len(p), len(s)):
            s_dict[s[right]] = s_dict.get(s[right], 0) + 1
            s_dict[s[left]] -= 1

            if s_dict[s[left]] == 0:
                del s_dict[s[left]]

            left += 1

            if p_dict == s_dict:
                sol_arr.append(left)

        return sol_arr
        