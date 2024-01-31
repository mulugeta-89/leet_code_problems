class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        maxi = -1
        count = 0
        freq = {}
        for right in range(len(fruits)):
            if fruits[right] not in freq:
                count += 1
            freq[fruits[right]] = freq.get(fruits[right],0) + 1
            while count > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                    count -= 1
                left += 1
            maxi = max(maxi, right-left+1)
        return maxi
        