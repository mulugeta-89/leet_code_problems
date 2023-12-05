class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        map = {"1":1, "2":2, "3":3,
                "4":4, "5":5, "6":6,
                "7":7, "8":8, "9":9, "0":0}
        value1 = 0
        res = 0
        for i in num1:
            value1 = value1 * 10 + map[i]
        for i in num2:
            res = res * 10 + value1 * map[i]
        return str(res)