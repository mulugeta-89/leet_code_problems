class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people_dict = {}
        for i in range(len(names)):
            people_dict[heights[i]] = names[i]
        people_dict = dict(sorted(people_dict.items(), key=lambda x: (x[0]), reverse=True))
        return list(people_dict.values())