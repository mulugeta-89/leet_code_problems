from collections import Counter
def common(words):
    data = Counter(words[0])
    for word in words:
        data2 = Counter(word)
        for key in data.keys():
            data[key] = min(data[key], data2[key])
    return data.elements()

print(common(["bella","label","roller"]))