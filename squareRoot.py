def squareRoot(number):
    root = 0
    if number == 1:
        root = 1
    for item in range(1,number):
        if item % 2 == 1:
            if number < item:
                break
            number -= item
            root += 1
            if number == 0:
                break
    return root
print(squareRoot(2147395599))


          
