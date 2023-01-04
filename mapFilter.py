from functools import reduce

arr = [1,5,4,3,5,6,7,5,3]
evens = list(filter(lambda x: x%2==0, arr))
odds = list(filter(lambda x: x%2 != 0, arr))
double_odds = list(map(lambda x: x*2, evens))
add_all_evens = reduce(lambda x, y: x + y, double_odds)
print(min([1,2,3,4,5]))
print(evens)
print(odds)
print(double_odds)
print(add_all_evens)