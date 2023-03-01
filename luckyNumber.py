def luckyNumbers(matrix):
    min_arr = []
    for item in matrix:
        min_arr.append(min(item))
    max_arr = [max(col) for col in zip(*matrix)]
    new_arr = min_arr + max_arr
    new_arr.sort()
    for i in range(len(new_arr)-1):
        if new_arr[i] == new_arr[i+1]:
            return [new_arr[i]]
    return []
        


print(luckyNumbers([[7,8],[1,2]]))