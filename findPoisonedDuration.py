def findPoisonedDuration(timeSeries, duration):
    counter = 0
    for i in range(len(timeSeries)-1):
        other_end = timeSeries[i]+duration-1
        for j in range(timeSeries[i], other_end+1):
            if j == timeSeries[i+1]:
                break
            else:
                counter += 1
    return counter + duration
print(findPoisonedDuration([1,2],2))