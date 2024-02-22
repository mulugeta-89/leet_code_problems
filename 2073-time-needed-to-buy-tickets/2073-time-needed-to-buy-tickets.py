class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        while tickets[k] != 0:
            mini = 0
            for i in range(len(tickets)):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    mini += 1
                if tickets[k] == 0:
                    break
            count += mini
        return count
        