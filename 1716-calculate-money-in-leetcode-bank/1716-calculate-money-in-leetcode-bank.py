class Solution:
    def totalMoney(self, num: int) -> int:
        quotient = num // 7
        upper = []
        days = 7
        sumi = 0
        for i in range(quotient):
            upper.append(days)
            days += 1
        for i in range(len(upper)):
            sumi += sum([i+1 for i in range(i, upper[i])])
        for i in range(num % 7):
            quotient +=1
            sumi += quotient
        return sumi
        