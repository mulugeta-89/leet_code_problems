def climbing_stairs(num):

    prev = 1
    next_prev = 2
    result = 0
    for i in range(2, num):
        result = prev + next_prev
        prev = next_prev
        next_prev = result
    return result
print(climbing_stairs(3))

