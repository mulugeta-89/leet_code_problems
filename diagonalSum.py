
def diagonalSum(mat):
    total = 0
    count = 0
    for item in mat:
        total += item[count]
        count += 1
    count2 = len(mat[0])-1
    for item in mat:
        total += item[count2]
        count2 -= 1
    if(len(mat)%2 != 0):
        total -= mat[len(mat)//2][len(mat[0])//2]
    return total
print(diagonalSum([[5]]))

