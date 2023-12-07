class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        for i in range(len(candies)):
            temp = candies[i] + extraCandies
            if temp >= maxi:
                candies[i] = True
            else:
                candies[i] = False
            temp = 0
        return candies
        