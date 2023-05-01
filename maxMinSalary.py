
def average(self, salary: List[int]) -> float:
    maxi = max(salary)
    mini = min(salary)
    soli = [item for item in salary if item != maxi and item != mini]
    sumi = sum(soli)
    return sumi/len(soli)