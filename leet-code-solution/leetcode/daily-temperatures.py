class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol_arr = [0] * len(temperatures)
        stack = []
        for i,x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                sol_arr[idx] = i-idx
            stack.append(i)
        return sol_arr