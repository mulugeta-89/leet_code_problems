class Bitset:

    def __init__(self, size: int):
        self.bits = ["0"] * size
        self.flipped = ["1"]*size
        self.size = size
        self.countOnes = 0
        

    def fix(self, idx: int) -> None:
        if self.bits[idx] == "0":
            self.bits[idx] = "1"
            self.flipped[idx] = "0"
            self.countOnes += 1
        

    def unfix(self, idx: int) -> None:
        if self.bits[idx] == "1":
            self.bits[idx] = "0"
            self.flipped[idx] = "1"
            self.countOnes -= 1

    def flip(self) -> None:
        self.bits, self.flipped = self.flipped, self.bits
        self.countOnes = self.size - self.countOnes
    def all(self) -> bool:
        return self.countOnes == self.size
    def one(self) -> bool:
        return self.countOnes > 0
        

    def count(self) -> int:
        return self.countOnes
        

    def toString(self) -> str:
        return "".join(self.bits)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()