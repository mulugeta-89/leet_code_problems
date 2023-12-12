class Solution:
    def isHappy(self, n: int) -> bool:
        running = 0
        while running <= 9:
            n = str(n)
            sum = 0
            for item in n:
                sum += pow(int(item), 2)
            if sum == 1:
                return True
            n = sum
            running += 1
        return False