class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_dict = dict(Counter(word1))
        word2_dict = dict(Counter(word2))
        return True if sorted(word2_dict.values()) == sorted(word1_dict.values()) and sorted(word1_dict.keys()) == sorted(word2_dict.keys()) else False