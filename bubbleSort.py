def bubbleSort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-i-1):
            if(num[j] > num[j+1]):
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num
print(bubbleSort([6,5,7,4,2,3,4,5,1,88,7,6,5,33,4,5]))