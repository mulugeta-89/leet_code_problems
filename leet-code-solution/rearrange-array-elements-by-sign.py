class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for item in nums:
            if item > 0:
                pos.append(item)
            else:
                neg.append(item)
        count = 1
        for i in range(len(neg)):
            pos.insert(count, neg[i])
            count += 2
        return pos
        