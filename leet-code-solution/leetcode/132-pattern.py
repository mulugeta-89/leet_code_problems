class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        other = float("inf")
        mini = float("inf")
        nums.reverse()
        for item in nums:
            while stack and stack[-1] < item:
                mini = stack.pop()
            if mini != other and item < mini:
                return True
            stack.append(item)
        return False
        