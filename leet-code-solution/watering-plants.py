class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        capacity_copy = capacity
        sol = 0
        #looping through each item of  plants array
        for i in range(len(plants)):
            # if capacity greater the capacity of specific item......i'll subtract it 
            if capacity >= plants[i]:
                capacity -= plants[i]
                sol += 1
            else:
                sol += i+(i+1)
                capacity = capacity_copy
                capacity -= plants[i]
        return sol
        