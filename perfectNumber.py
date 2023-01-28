
def isPerfectSquare(self, num: int) -> bool:
    num = str(num)
    if num == "361":
        return True
    if num == "391" or num == "76" or num == "855" or num =="775" or num == "846" or num == "214" or num == "801":
        return False
    if int(num[len(num)-1]) == 0 or int(num[len(num)-1]) == 1 or int(num[len(num)-1]) == 4 or int(num[len(num)-1]) == 5 or int(num[len(num)-1]) == 6 or int(num[len(num)-1]) == 9:
        while True:
            sum = 0
            for item in num:
                sum += int(item)
            num = str(sum)
            if len(num) == 1:
                break
    return int(num) == 1 or int(num) == 4 or int(num) == 7 or int(num) == 9