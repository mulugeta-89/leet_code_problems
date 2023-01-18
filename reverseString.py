def reverseString(word):
    #word = list(word)
    # for i in range(len(word)):
    #     temp = word[i]
    #     word[i] = word[len(word)-i-1]
    #     word[len(word)-i-1] = temp
    # return word
    left = 0
    right = len(word)-1
    while left < right:
        # temp = word[left]
        # word[left] = word[right]
        # word[right] = temp
        word[left], word[right] = word[right], word[left]
        left += 1
        right -=1
print(reverseString("hello"))