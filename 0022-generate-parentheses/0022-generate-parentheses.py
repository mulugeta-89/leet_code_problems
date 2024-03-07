class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        def backtrack(open, close, stri):
            if len(stri) == 2*n :
                arr.append(stri)
            else:
                if open < n:
                    backtrack(open+1, close, stri+"(")
                if close < open:
                    backtrack(open, close+1, stri+")")
        backtrack(0,0,"")
        return arr
                    
            