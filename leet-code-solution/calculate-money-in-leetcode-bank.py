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
            sumi += (7 * (upper[i]+(upper[i]-6)) // 2)
        for i in range(num % 7):
            quotient +=1
            sumi += quotient
        return sumi
        