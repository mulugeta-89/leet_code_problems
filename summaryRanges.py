def summaryRanges(arr):
    new_arr = []
    j = 0
    for i in range(len(arr)):
        if i+1==len(arr) or arr[i]+1!=arr[i+1]:
            if j==i:
                new_arr.append(str(arr[i]))
            else:
                new_arr.append(str(arr[j])+"->"+str(arr[i]))
            j=i+1
    return new_arr
print(summaryRanges([0,2,3,4,6,8,9]))

            
