def romanToInteger(s):
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    s = s.replace("IV", "IIII").replace("IX", "VIII").replace("XL", "XXXX").replace("XC","LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    return sum(map(lambda x: romans[x], s))
print(romanToInteger("MCM"))