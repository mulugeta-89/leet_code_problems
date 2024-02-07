class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
            alphabet_dict = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h',
        8: 'i',
        9: 'j',
        10: 'k',
        11: 'l',
        12: 'm',
        13: 'n',
        14: 'o',
        15: 'p',
        16: 'q',
        17: 'r',
        18: 's',
        19: 't',
        20: 'u',
        21: 'v',
        22: 'w',
        23: 'x',
        24: 'y',
        25: 'z'
    }
            arr = [0] * len(s)
            for shift in shifts:
                a,b,k = shift
                if k == 0:
                    arr[a] += -1
                    if b != len(s)-1:
                        arr[b+1] += 1
                else:
                    arr[a] += 1
                    if b != len(s)-1:
                        arr[b+1] -= 1
            for i in range(1, len(arr)):
                arr[i] = arr[i-1] + arr[i]
            sol_str = ""
            for i in range(len(arr)):
                sol_str += alphabet_dict[(ord(s[i]) - ord('a') + arr[i]) %26]
            return sol_str