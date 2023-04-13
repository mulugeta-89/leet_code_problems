def stringMaching(words):
    sol_arr = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            if words[i] in words[j]:
                sol_arr.append(words[i])
    return list(set(sol_arr))
            
print(stringMaching(["blue","green","bu"]))