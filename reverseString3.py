def reverseString(s):
    s = s.split(" ")
    new_s = []
    for item in s:
        new_s.append(item[::-1])
    return " ".join(new_s)
print(reverseString("Let's take LeetCode contest"))