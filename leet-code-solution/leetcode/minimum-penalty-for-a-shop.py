class Solution:
    def bestClosingTime(self, customers: str) -> int:
        sol = 0
        running_score = 0
        ind = -1
        for i in range(len(customers)):
            running_score += 1 if customers[i] == "Y" else -1
            if running_score > sol:
                sol = running_score
                ind = i
        return ind+1
    
        