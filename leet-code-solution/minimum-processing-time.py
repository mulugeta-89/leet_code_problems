class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        n = len(processorTime)-1
        maxi = -1
        for i in range(3,len(tasks),4):
            maxi = max(maxi, tasks[i]+processorTime[n])
            n -= 1
        return maxi
        