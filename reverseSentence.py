def reverse(s):
    s = s.split(" ")
    s = list(filter(lambda x: x != "", s))
    s[:] = s[::-1]
    return " ".join(s)
        
print(reverse("a good   example"))
