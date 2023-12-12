class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        dicti = Counter(arr)
        for k in dicti:
            if ((dicti[k]/n)*100) > 25:
                return k
        
        