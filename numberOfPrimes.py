def is_prime(num):
    if num > 2:
        for i in range(2, num):
            if num%i==0:
                return False
    return True

def primes(num):
    if num < 2:
        return 0
    counter = 0
    for i in range(2,num):
        if is_prime(i):
            counter += 1
    return counter
print(primes(10))
