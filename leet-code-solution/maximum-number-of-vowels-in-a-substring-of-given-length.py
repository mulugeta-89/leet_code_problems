class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        vowel_count = 0
        left = 0
        maxi = 0
        for right in range(len(s)):
            if s[right] in vowels:
                vowel_count += 1
            while right-left + 1 > k:
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1
            maxi = max(maxi, vowel_count)
        return maxi
        