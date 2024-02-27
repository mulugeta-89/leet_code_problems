class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rad = [i for i in range(len(senate)) if senate[i] == "R"]
        dire = [i for i in range(len(senate)) if senate[i] == "D"]
        while rad and dire:
            r_i = rad.pop(0)
            d_i = dire.pop(0)
            if r_i < d_i:
                n += 1
                rad.append(n)
            else:
                n+=1
                dire.append(n)
        return "Radiant" if rad else "Dire"