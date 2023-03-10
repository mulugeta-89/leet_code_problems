def insertInterval(intervals, newInterval):
    intervals = intervals + [newInterval]
    intervals.sort()
    sol_arr = []
    for interval in intervals:
        if sol_arr and sol_arr[-1][1] >= interval[0]:
            sol_arr[-1][1] = max(sol_arr[-1][1], interval[1])
        else:
            sol_arr.append(interval)
    return sol_arr

print(insertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))