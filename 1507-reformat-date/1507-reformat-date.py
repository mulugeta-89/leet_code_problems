class Solution:
    def reformatDate(self, date: str) -> str:
        Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        sol = ""
        date = date.split()
        third = date[2]
        second = Month.index(date[1])+1
        if second < 10:
            second = "0"+ str(second)
        second = str(second)
        first = ""
        for item in date[0]:
            if item.isdigit():
                first += (item)
        if int(first) < 10:
            first = "0" + str(first)
        first = str(first)
        sol = third +"-"+second+"-"+first
        return sol
        
        