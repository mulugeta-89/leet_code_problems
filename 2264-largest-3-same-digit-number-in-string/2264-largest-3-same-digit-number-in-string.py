class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxi = -float("inf")
        for i in range(len(num)-2):
            if len(set(num[i: i+3])) == 1:
                sub = num[i:i+3]
                maxi = max(int(sub[0]), maxi)
        return str(maxi)*3 if maxi >= 0 else ""
        