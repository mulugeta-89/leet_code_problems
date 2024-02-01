left = 0
        max_count = 0
        sol = -1
        freq = {}
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_count = max(max_count, freq[s[right]])
            while right-left+1 - max_count > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            sol = max(sol, right-left+1)
        return sol