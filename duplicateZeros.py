
def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    if set(arr) != {0}:
        i = 0
        new_arr = arr.copy()
        arr.clear()
        while i < len((new_arr)):
            if new_arr[i] == 0:
                arr.append(0)
                arr.append(0)
            else:
                arr.append(new_arr[i])
            if len(arr) == len(new_arr):
                break
            i += 1
        arr[:] = arr[:len(new_arr)]
    
    
        
    