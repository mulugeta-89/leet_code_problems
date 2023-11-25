class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        sol_arr = []
        words1_dict = Counter(words1)
        words2_dict = Counter(words2)
        words1_dict = {k:v for k,v in words1_dict.items() if v==1}
        words2_dict = {k:v for k,v in words2_dict.items() if v==1}
        w1 = list(words1_dict.keys())
        w2 = list(words2_dict.keys())
        for item in w1:
            if item in w2:
                sol_arr.append(item)
        for item in w2:
            if item in w1:
                sol_arr.append(item)
        return len(set(sol_arr))
        
        