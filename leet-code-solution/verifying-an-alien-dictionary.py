class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {key: val for val, key in enumerate(order)}
        def findIndex(s):
            return [order_dict[char] for char in s]
        return sorted(words,key=findIndex) == words
        