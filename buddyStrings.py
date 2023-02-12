def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal:
        return True if len(s) -len(set(goal)) >= 1 else False
    diff = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff.append(i)
    if len(diff) > 2 or len(diff)!= 2:
        return False
    if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
        return True
    return False
    



print(buddyStrings("ab","ba"))