words = ["flower","flow","flight"]
words.sort()
print(words)
def longestPrefix(strs):
    prefix = ""
    strs.sort()
    for i in range(len(strs[0])):
        if strs[0][i] == strs[1][i]:
            prefix += strs[0][i]
        else:
            break
    return prefix
    
        
        
print(longestPrefix(words))