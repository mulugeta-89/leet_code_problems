class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        if len(deck) == 1:
            return deck
        starter = deque()
        starter.append(deck[1])
        starter.append(deck[0])
        
        for i in range(2,len(deck)):
            prev = deque()
            prev.append(starter[-1])
            for j in range(len(starter)-1):
                prev.append(starter[j])
            prev.appendleft(deck[i])
            starter = prev
        return starter
        