def removeDuplicate(s):
    last_occur = {}
    stack = []
    visited = set()
    for i in range(len(s)):
        last_occur[s[i]] = i
    for i in range(len(s)):
        if s[i] not in visited:
            if(stack and stack[-1] > s[i] and last_occur[stack[-1]] > i):
                visited.remove(stack.pop())
            stack.append(s[i])
            visited.add(s[i])
    return "".join(stack)
print(removeDuplicate("cbacdcbcd"))