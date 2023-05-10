def spiral(n):
    matrix = []
    small_arr = []
    for i in range(1, n**2 + 1):
        small_arr.append(0)
        if len(small_arr) == n:
            matrix.append(small_arr)
            small_arr = []
    rowBegin = 0
    rowEnd = n-1
    columnBegin = 0
    columnEnd = n-1
    count = 1
    while rowBegin <= rowEnd and columnBegin <= columnEnd:
        for i in range(columnBegin, columnEnd+1):
            matrix[rowBegin][i] = count
            count+=1
        rowBegin+=1

        for i in range(rowBegin, rowEnd+1):
            matrix[i][columnEnd] = count
            count += 1
        columnEnd -= 1

        for i in range(columnEnd, columnBegin-1,-1):
            matrix[rowEnd][i] = count
            count += 1
        rowEnd -= 1
        for i in range(rowEnd, rowBegin-1,-1):
            matrix[i][columnBegin] = count
            count += 1
        columnBegin+= 1
    return matrix

print(spiral(3))