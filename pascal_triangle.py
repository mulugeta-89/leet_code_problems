
def pascal_triangle(num):
    all_array = []
    for i in range(1,num):
        if i == 1:
            all_array.append([1])
        if i == 2:
            all_array.append([1,1])
        if i > 2:
            new_arr =[]
            new_arr.append(1)
            working_arr = all_array[len(all_array)-1]
            for i in range(len(working_arr)-1):
                new_arr.append(working_arr[i] + working_arr[i+1])
            new_arr.append(1)
            all_array.append(new_arr)
    return all_array
print(pascal_triangle(5))
        
    
            