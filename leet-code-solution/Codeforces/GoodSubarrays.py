from collections import defaultdict
from itertools import accumulate

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    s = input()
    s = [int(x) for x in s]

    
    sol = 0
    dicti = defaultdict(int)
    prefix_sum = list(accumulate(s))
    prefix_sum.insert(0,0)
    for i in range(len(prefix_sum)):
        dicti[prefix_sum[i]-i] += 1
    for v in dicti.values():
        sol += v*(v-1)//2
    print(sol)