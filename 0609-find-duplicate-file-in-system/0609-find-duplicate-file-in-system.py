class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        other_arr = []
        for item in paths:
            duplicate = item.split()
            temp1 = duplicate[0]
            for i in range(1, len(duplicate)):
                temp = temp1 + "/" + duplicate[i]
                other_arr.append(temp)
        dicti = {}
        for item in other_arr:
            index1 = item.index("(")
            index12 = item.index(")")
            key1 = item[index1+1:index12]
            if key1 not in dicti:
                dicti[key1] = [1, item[:index1]]
            else:
                dicti[key1][0] += 1
                dicti[key1].append(item[:index1])
        sol_arr = []
        for key in dicti.keys():
            temp = []
            if dicti[key][0] > 1:
                for i in range(1, len(dicti[key])):
                    temp.append(dicti[key][i])
            if temp != []:
                sol_arr.append(temp)
        return sol_arr
        