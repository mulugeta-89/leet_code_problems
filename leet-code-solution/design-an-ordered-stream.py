class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None]*n
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        ans =[]
        while self.ptr < len(self.arr) and self.arr[self.ptr] is not None:
            ans.append(self.arr[self.ptr])
            self.ptr += 1
        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)