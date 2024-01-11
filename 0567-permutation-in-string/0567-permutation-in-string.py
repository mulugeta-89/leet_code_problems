class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        s2_dict = {}
        left = 0
        for i in range(len(s1)):
            s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
            s2_dict[s2[i]] = s2_dict.get(s2[i],0) + 1
        if s1_dict == s2_dict:
            return True
        for right in range(len(s1), len(s2)):
            s2_dict[s2[right]] = s2_dict.get(s2[right], 0) + 1
            s2_dict[s2[left]] -= 1

            if s2_dict[s2[left]] == 0:
                del s2_dict[s2[left]]
            left += 1
            if s1_dict == s2_dict:
                return True
        return False
        