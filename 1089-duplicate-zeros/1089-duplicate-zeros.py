class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        new_arr = []
        for item in arr:
            if item != 0:
                new_arr.append(item)
            else:
                new_arr.append(0)
                new_arr.append(0)
        arr[:] = new_arr[:len(arr)]
       
            
        