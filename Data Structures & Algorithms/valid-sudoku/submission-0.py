class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for j in range(0,9):
            s=set()
            for i in range(0,9):
                if board[i][j]==".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        for i in range(0,9):
            s=set()
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        for row in range(0,9,3):
            for column in range(0,9,3):
                s=set()
                for i in range(3):
                    for j in range(3):
                        val=board[row+i][column+j]
                        if val==".":
                            continue
                        if val in s:
                            return False
                        s.add(val)
        return True
        