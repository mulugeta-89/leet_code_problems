def stringCompare(s,t):
    s_stack = []
    t_stack = []
    for item in s:
        if not s_stack and item == "#":
            continue
        if item == "#":
            s_stack.pop()
            continue
        s_stack.append(item)
    for item in t:
        if not t_stack and item == "#":
            continue
        if item == "#":
            t_stack.pop()
            continue
        t_stack.append(item)
        
    return s_stack == t_stack
print(stringCompare("a#c", "b"))