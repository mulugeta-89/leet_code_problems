def number(n):
    nums = set(range(2, n))
    counter = 0
    while nums:
        prime = min(nums)
        counter += 1
        nums -= set(range(prime, n+1, prime))
    return counter
print(number(10))