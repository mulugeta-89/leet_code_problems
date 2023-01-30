def self_deviding(num1, num2):
    result = []
    for item in range(num1, num2+1):
        item = str(item)
        if "0" in item:
            continue
        flag = False
        for little_item in item:
            if int(item)%int(little_item)!=0:
                flag = False
                break
            else:
                flag = True
        if flag:
            result.append(int(item))
    return result
print(self_deviding(1,22))

        

