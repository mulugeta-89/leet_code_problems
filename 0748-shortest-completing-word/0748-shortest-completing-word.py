def checkall(licensePlate, word):
    word = list(word)
    for item in licensePlate:
        if item in word:
            word.remove(item)
        else:
            return False
    return True
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        sol_arr = []
        new_license = ""
        for item in licensePlate:
            if not item.isdigit() and item != " ":
                new_license+=item.lower()
        for item in words:
            upper = checkall(new_license, item)
            if upper:
                sol_arr.append(item)
        sol_arr = sorted(sol_arr, key=len)
        return sol_arr[0]