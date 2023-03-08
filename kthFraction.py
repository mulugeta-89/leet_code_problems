from fractions import Fraction
def fraction(arr,k):
    sol_arr = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            sol_arr.append(arr[i]/arr[j])
    sol_arr = sorted(sol_arr)
    smallest = sol_arr[k-1]
    sol = str(Fraction(str(smallest)).limit_denominator())
    numerator, denominator = sol.split("/")
    return [int(numerator), int(denominator)]
print(fraction([1,2,3,5],3))
