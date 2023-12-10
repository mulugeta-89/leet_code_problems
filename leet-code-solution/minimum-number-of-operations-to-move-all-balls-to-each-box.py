class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        sol_arr = [0] * len(boxes)
        for i in range(len(boxes)):
            temp = 0
            for j in range(len(boxes)):
                if i == j:
                    continue
                if boxes[j] == "1":
                    temp += abs(j-i)
            sol_arr[i] = temp
        return sol_arr
        