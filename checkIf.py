def checkIf(arr):

    count = 0
    for item in arr:
        count += 1
        if item /2 in arr[count:] or item*2 in arr[count:]:
            return True
    return False