class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dicti = {}
        for item in matches:
            if item[0] not in dicti:
                dicti[item[0]] = [1, 0]
            else:
                dicti[item[0]][0] += 1
            if item[1] not in dicti:
                dicti[item[1]] = [0,1]
            else:
                dicti[item[1]][1] += 1
        winners = []
        lose_one = []
        for key in dicti.keys():
            if dicti[key][1] == 0:
                winners.append(key)
            elif dicti[key][1] == 1:
                lose_one.append(key)
            else:
                continue
        winners.sort()
        lose_one.sort()
        return [winners, lose_one]
        