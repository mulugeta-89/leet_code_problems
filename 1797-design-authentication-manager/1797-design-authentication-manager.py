class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.timetolive = timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = [currentTime, currentTime+self.timetolive]
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if self.tokens[tokenId][1] > currentTime:
                self.tokens[tokenId] = [currentTime, currentTime+self.timetolive]
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for k in self.tokens:
            if self.tokens[k][0] <= currentTime < self.tokens[k][1]:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)