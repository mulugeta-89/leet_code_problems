class FrequencyTracker:

    def __init__(self):
        self.dicti = {}
        self.freq = {}

    def add(self, number: int) -> None:
        if number in self.dicti:
            prev_freq = self.dicti[number]
            self.dicti[number] += 1
            new_freq = self.dicti[number]
            self.freq[prev_freq] -= 1
            if self.freq[prev_freq] == 0:
                del self.freq[prev_freq]
            self.freq.setdefault(new_freq, 0)
            self.freq[new_freq] += 1
        else:
            self.dicti[number] = 1
            self.freq.setdefault(1, 0)
            self.freq[1] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.dicti:
            current_freq = self.dicti[number]
            if current_freq == 1:
                del self.dicti[number]
            else:
                self.dicti[number] -= 1

            self.freq[current_freq] -= 1
            if self.freq[current_freq] == 0:
                del self.freq[current_freq]
                
            if current_freq - 1 > 0:
                self.freq.setdefault(current_freq - 1, 0)
                self.freq[current_freq - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq
