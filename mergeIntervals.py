def merging(intervals):
    intervals.sort()
    sol_arr = []
    for interval in intervals:
        if sol_arr and sol_arr[-1][1] > interval[0]:
            sol_arr[-1][1] = max(sol_arr[-1][1], interval[1])
        else:
            sol_arr.append(interval)
    return sol_arr
print(merging([[1,4],[0,2],[3,5]]))

