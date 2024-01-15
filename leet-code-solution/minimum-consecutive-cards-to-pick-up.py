class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        freq = {}
        sol = float("inf")
        for right in range(len(cards)):
            freq[cards[right]] = freq.get(cards[right],0) + 1
            while freq[cards[right]] == 2:
                sol = min(sol, right-left+1)
                freq[cards[left]] -= 1
                if freq[cards[left]] == 0:
                    del freq[cards[left]]
                left += 1
        return sol if sol != float("inf") else -1