def linearSearch(num, target):
    location = -1
    i = 0
    while(i < len(num) and num[i] != target):
        i += 1
    if i < len(num):
        location = i
    return location

print(linearSearch([1,2,3,4,5,6], 8))
