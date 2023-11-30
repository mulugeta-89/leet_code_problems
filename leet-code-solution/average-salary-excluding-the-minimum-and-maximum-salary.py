class Solution:
    def average(self, salary: List[int]) -> float:
        # maxi = max(salary)
        # mini = min(salary)
        # soli = [item for item in salary if item != maxi and item != mini]
        salary.sort()
        sol = 0
        for i in range(1, len(salary)-1):
            sol += salary[i]

        return sol/(len(salary)-2)