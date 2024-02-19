class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        other = palindrome.copy()
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)):
            if palindrome[i] != "a":
                palindrome[i] = "a"
                break
        if len(set(palindrome)) == 1 and set(palindrome) == {"a"}:
            other[-1] = "b"
            return "".join(other)
        return "".join(palindrome)
        