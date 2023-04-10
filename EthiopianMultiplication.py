def ethiop(a,b):
    a_arr = []
    b_arr = []
    new_arr = []
    while a > 1:
        a = a//2
        a_arr.append(a)
    for item in a_arr:
        b = b*2
        b_arr.append(b)
    for idx,item in enumerate(a_arr):
        if item%2!=0:
            new_arr.append(b_arr[idx])
    return sum(new_arr)