def prefix(A, B):
    sol_arr = []
    running = []
    count = 0
    for i in range(len(A)):
        running += A[:i+1]
        running += B[:i+1]
        running = list(set(running))
        for item in running:
            if item in A[:i+1] and item in B[:i+1]:
                count += 1
        sol_arr.append(count)
        running = []
        count = 0
    return sol_arr
print(prefix([1,3,2,4],[3,1,2,4]))