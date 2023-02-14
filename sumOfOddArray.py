
def sumOddLengthSubarrays(arr):
    total = 0
    for i in range(1, len(arr)+1,2):
        for j in range(len(arr)-i+1):
            total += sum(arr[j:j+i])
    return total

        
        
