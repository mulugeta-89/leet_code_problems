from collections import defaultdict

def sorting(mat):
    d = defaultdict(list) # this makes 
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            d[i-j].append(mat[i][j])
    for item in d:
        d[item].sort(reverse=True)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = d[i-j].pop()
    return mat
print(sorting([[3,3,1,1],[1,1,1,1],[1,1,1,2]]))
