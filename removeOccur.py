def removeOccurrence(s,part):
    stack = ""
    for item in s:
        stack += item
        if part in "".join(stack):
            stack = stack.replace(part, "")
    return stack

print(removeOccurrence("aabababa","aba"))