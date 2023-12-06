class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        word1 = set("qwertyuiop")
        word2 = set("asdfghjkl")
        word3 = set("zxcvbnm")
        new_arr = []
        for item in words:
            item2 = set(item.lower())
            if item2 <= word1 or item2 <= word2 or item2 <= word3:
                new_arr.append(item)
        return new_arr
