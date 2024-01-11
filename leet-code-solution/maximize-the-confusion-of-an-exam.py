class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        freq = {"T": 0, "F": 0}
        sol1 = 0
        for right in range(len(answerKey)):
            freq[answerKey[right]] += 1
            while freq["F"] > k:
                freq[answerKey[left]] -= 1
                left += 1
            sol1 = max(sol1, right-left+1)
        left1 = 0
        freq1 = {"T": 0, "F": 0}
        sol2 = 0

        for right in range(len(answerKey)):
            freq1[answerKey[right]] += 1

            while freq1["T"] > k:
                freq1[answerKey[left1]] -= 1
                left1 += 1

            sol2 = max(sol2, right-left1+1)
        return max(sol1, sol2)
        