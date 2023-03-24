from collections import Counter
import math
def percentageOfLetter(s, letter):
    if letter not in s:
        return 0
    s_dict = dict(Counter(s))
    result = (s_dict[letter] / len(s)) * 100
    return int(math.floor(result))

print(percentageOfLetter("jjjj", "o"))