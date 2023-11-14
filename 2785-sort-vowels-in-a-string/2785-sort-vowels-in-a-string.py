class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["a", "e","i","o","u", "A", "E","I","O","U"]
        voweli = []
        for item in s:
            if item in vowels:
                voweli.append(item)
        voweli = sorted(voweli, key=lambda x: ord(x))
        k = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = voweli[k]
                k += 1
        return "".join(s)
        