class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = "".join(map(lambda x: str(x), digits))
        res = str(int(digit)+1)
        return [int(x) for x in res]
        