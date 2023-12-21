class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            temp = []
            for j in range(len(strs)):
                temp += strs[j][i]
            for i in range(1, len(temp)):
                if temp[i-1] > temp[i]:
                    count += 1
                    break
        return count
        