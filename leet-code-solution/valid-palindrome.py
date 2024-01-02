class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = "".join(filter(str.isalnum, s.lower()))
        for i in range(len(newString)):
            if newString[i] != newString[len(newString)-i-1]:
                return False
        return True