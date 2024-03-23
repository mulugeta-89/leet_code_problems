class TimeMap:

    def __init__(self):
        self.dicti = defaultdict(list)
    def binarySearch1(self, key, val):
        if self.dicti[key]:
            l, r = 0, len(self.dicti[key][1])-1
            while l <= r:
                mid = (l+r)//2
                if val < self.dicti[key][1][mid]:
                    r = mid-1
                else:
                    l = mid+1
            return r
        return -1

    def set(self, key: str, value: str, timestamp: int) -> None:
        if len(self.dicti[key]) == 2:
            self.dicti[key][0].append(value)
            self.dicti[key][1].append(timestamp)
        else:
            self.dicti[key].append([value])
            self.dicti[key].append([timestamp])        
    def get(self, key: str, timestamp: int) -> str:
        pos = self.binarySearch1(key, timestamp)
        return self.dicti[key][0][pos] if pos != -1 else ""