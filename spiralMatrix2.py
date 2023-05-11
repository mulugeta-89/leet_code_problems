def spiral(n):
    matrix = [[0] *n for i in range(n)]
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