class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        tot = sum(cardPoints)
        left = 0
        n = len(cardPoints)
        curr_sum = 0
        for i in range(n-k):
            curr_sum += cardPoints[i]
        sol = tot-curr_sum
        for right in range(n-k, len(cardPoints)):
            curr_sum += cardPoints[right]
            curr_sum -= cardPoints[left]
            left += 1
            sol = max(sol, tot-curr_sum)
        return sol
        