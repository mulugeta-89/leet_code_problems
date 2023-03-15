def sumOf(num):
    if num %3 == 0:
        div = num//3
        return [div-1, div, div+1]
    else:
        return []
print(sumOf(4))
