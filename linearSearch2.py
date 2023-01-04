def linearSearch(num, target):
    for item in num:
        if item == target:
            return True
    return False
print(linearSearch([1,2,3,4,5,6], 2))