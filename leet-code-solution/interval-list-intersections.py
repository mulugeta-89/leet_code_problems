class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        sol_arr = []
        l,r = 0, 0
        while l < len(firstList) and r < len(secondList):
            start1, end1 = firstList[l]
            start2, end2 = secondList[r]
            starting = max(start1, start2)
            ending = min(end1, end2)
            if starting <= ending:
                sol_arr.append([starting, ending])

            if end1 < end2:
                l += 1
            else:
                r += 1
        return sol_arr
        