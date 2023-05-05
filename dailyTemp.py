def dailyTemp(tempratures):
    sol_arr = [0 for i in range(len(tempratures))]
    for i in range(len(tempratures)-1):
        count = 0
        for j in range(i+1, len(tempratures)):
            count += 1
            if tempratures[j] > tempratures[i]:
                sol_arr[i] = count
                break
    return sol_arr
#alternative


    stack = []
    for i,x in enumerate(tempratures):
        while stack and tempratures[stack[-1]] < tempratures[i]:
            idx = stack.pop()
            sol_arr[idx] = i-idx
        stack.append(i)
    return sol_arr

print(dailyTemp([73,74,75,71,69,72,76,73]))