import math
def trimMean(arr):
    arr.sort()
    n = len(arr)
    theFiveth = math.floor(n * 0.05)
    remaining2 = arr[theFiveth:-theFiveth]
    return (sum(remaining2)/len(remaining2))
    
print(trimMean([6,0]))