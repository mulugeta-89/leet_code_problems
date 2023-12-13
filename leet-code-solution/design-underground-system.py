class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.travel_times = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkinTime = self.checkins[id]
        if (startStation, stationName) in self.travel_times:
            self.travel_times[(startStation, stationName)][0] += t - checkinTime
            self.travel_times[(startStation, stationName)][1] += 1
        else:
            self.travel_times[(startStation, stationName)] = [t-checkinTime, 1]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.travel_times:
            return self.travel_times[(startStation, endStation)][0]/ self.travel_times[(startStation, endStation)][1]
        else:
            return 0.0
            
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)