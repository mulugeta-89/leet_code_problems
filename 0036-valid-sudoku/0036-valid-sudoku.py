def returner(lister):
    lister_dict = Counter(lister)
    for k in lister_dict.keys():
        if k == ".":
            continue
        if lister_dict[k] > 1:
            return False
    return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            temp_dict = dict(Counter(board[i]))
            keys = list(temp_dict.keys())
            for k in keys:
                if k == ".":
                    continue
                if temp_dict[k] > 1:
                    return False 
        for i in range(len(board)):
            temp_arr = []
            for j in range(len(board)):
                temp_arr.append(board[j][i])
            temp_dict = Counter(temp_arr)
            keys = list(temp_dict.keys())
            for k in keys:
                if k == ".":
                    continue
                if temp_dict[k] > 1:
                    return False
        temp = []
        temp1 = []
        temp2 = []
        for i in range(3):
            for j in range(9):
                if j >= 0 and j < 3:
                    temp.append(board[i][j])
                if j >= 3 and j < 6:
                    temp1.append(board[i][j])
                if j >= 6:
                    temp2.append(board[i][j])
        if returner(temp) == False or returner(temp2) == False or returner(temp1) == False:
            return False
        temp = []
        temp1 = []
        temp2 = []
        for i in range(3, 6):
            for j in range(9):
                if j >= 0 and j < 3:
                    temp.append(board[i][j])
                if j >= 3 and j < 6:
                    temp1.append(board[i][j])
                if j >= 6:
                    temp2.append(board[i][j])
        if returner(temp) == False or returner(temp2) == False or returner(temp1) == False:
            return False
        temp = []
        temp1 = []
        temp2 = []
        for i in range(6, 9):
            for j in range(9):
                if j >= 0 and j < 3:
                    temp.append(board[i][j])
                if j >= 3 and j < 6:
                    temp1.append(board[i][j])
                if j >= 6:
                    temp2.append(board[i][j])
        if returner(temp) == False or returner(temp2) == False or returner(temp1) == False:
            return False
        return True