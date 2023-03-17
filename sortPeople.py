
def sortPeople(names, heights):
    people_dict = {}
    for i in range(len(names)):
        people_dict[heights[i]] = names[i]
    people_dict = dict(sorted(people_dict.items(), key=lambda x: (x[0]), reverse=True))
    return list(people_dict.values())
    
print(sortPeople(["Alice","Bob","Bob"], [155,185,150]))
