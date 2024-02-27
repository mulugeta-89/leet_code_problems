class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        total_array = []
        for i in range(1,rowIndex+2):
            if i == 1:
                total_array.append([1])
            if i == 2:
                total_array.append([1,1])
            if i > 2:
                new_array = []
                working_array = total_array[len(total_array)-1]
                new_array.append(1)
                for i in range(len(working_array)-1):
                    new_array.append(working_array[i] + working_array[i+1])
                new_array.append(1)
                total_array.append(new_array)
        return total_array[rowIndex]