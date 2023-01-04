def palindrom(num):
    num = str(num)
    for i in range(len(num)):
        if num[i] != num[len(num)-i-1]:
            return False
        return True    
print(palindrom(12))

print(len(str(12)))
