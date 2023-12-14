class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sol_arr = []
        dicti = {}
        for item in cpdomains:
            splitted = item.split(" ")
            sol_arr.append(item)
            indi_of_dot = [ind for ind, val in enumerate(splitted[1]) if val == "."]
            for i in range(len(indi_of_dot)):
                sol_arr.append(splitted[0] + " " + splitted[1][indi_of_dot[i]+1:])
        for item in sol_arr:
            splitted = item.split(" ")
            if splitted[1] in dicti:
                dicti[splitted[1]] += int(splitted[0])
            else:
                dicti[splitted[1]] = int(splitted[0])
        res = []
        for key, val in dicti.items():
            temp = str(val) + " " + key
            res.append(temp)
            temp = ""
        return res
        