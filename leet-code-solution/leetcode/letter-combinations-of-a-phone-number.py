class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dicti = {
        "2": "abc ",
        "3": "def ",
        "4": "ghi ",
        "5": "jkl ",
        "6": "mno ",
        "7": "pqrs",
        "8": "tuv ",
        "9": "wxyz"
    }
        sol_arr = []
        k = len(digits)
        def backtrack(root,path):
            if len(path) == k:
                trimmed = ""
                for i in path:
                    if i != " ":
                        trimmed += i
                if len(trimmed) == k:
                    sol_arr.append(trimmed)
                return
            for i in range(len(dicti[digits[0]])):
                if dicti[digits[root]][i]:
                    path.append(dicti[digits[root]][i])
                    backtrack(root+1,path)
                    path.pop()
        if k > 0:
            backtrack(0,[])
        return sol_arr
        