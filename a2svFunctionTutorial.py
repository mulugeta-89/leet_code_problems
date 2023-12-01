def smallestMultiple(n):
    return n*2 if n%2 != 0 else n
def evenOdd(n):
        if n%2 != 0:
            return "Weird"
        elif n%2 == 0 and 2 <= n <= 5:
            return "Not Weird"
        elif n%2 == 0 and 6 <= n <= 20:
            return "Weird"
        else:
            return "Not Weird"
def printPowers(n):
     for i in range(n):
        print(i**2)
print(evenOdd(24))