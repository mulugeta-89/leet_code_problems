
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, i, j , idx, visited):
            if idx == len(word)-1:
                return True
            visited[i][j] = True
            if i > 0 and visited[i-1][j] == False and board[i-1][j] == word[idx+1]:
                if dfs(board, word, i-1 , j, idx+1, visited):
                    return True
            if j > 0 and visited[i][j-1] == False and board[i][j-1] == word[idx+1]:
                if dfs(board, word, i , j-1, idx+1, visited):
                    return True
            if i < len(board)-1 and visited[i+1][j] == False and board[i+1][j] == word[idx+1]:
                if dfs(board, word, i+1 , j, idx+1, visited):
                    return True
            if j < len(board[0])-1 and visited[i][j+1] == False and board[i][j+1] == word[idx+1]:
                if dfs(board, word, i , j+1, idx+1, visited):
                    return True
            visited[i][j] = False
            return False
        r = len(board)
        c = len(board[0])
        visited = [[False for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0] and dfs(board, word, i , j, 0, visited):
                    return True
        return False

        