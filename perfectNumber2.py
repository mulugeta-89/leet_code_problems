def perfectNumber(num):
    sol_arr = [i for i in range(1,int(num/2)+1) if num%i==0]
    return sum(sol_arr) == num
print(perfectNumber(28))