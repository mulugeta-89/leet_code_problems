def sortSentence(s):
    sol_arr = []
    s = s.split(" ")
    s = sorted(s, key=lambda x: x[-1])
    for item in s:
        stri = ""
        for little in item:
            if little.isalpha():
                stri+=little
        sol_arr.append(stri)
    return " ".join(sol_arr)

print(sortSentence("is2 sentence4 This1 a3"))