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
    s = list(s)
    total = 0
    for item in s:
        if item == "I":
            total += romans["I"]
        if item == "V":
            total += romans["V"]
        if item == "X":
            total += romans["X"]
        if item == "L":
            total += romans["L"]
        if item == "C":
            total += romans["D"]
        if item == "D":
            total += romans["D"]
        if item == "M":
            total += romans["D"]
    return total
print(romanToInteger("M"))