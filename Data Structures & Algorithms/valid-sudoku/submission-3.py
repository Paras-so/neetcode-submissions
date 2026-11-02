class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #BRUTE FORCE
        
       def checkRows(board): 
            for i in range(9):
                seen = set()
                for j in range(9):
                    if board[i][j] == "." :
                        continue
                    elif board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True

       def checkCol(board):
            for j in range(9):
                seen = set()
                for i in range(9):
                    if board[i][j] == "." :
                        continue
                    elif board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True
       def checkBox(board):
            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    seen = set()
                    for i in range(row, row+3):
                        for j in range(col, col+3):
                            if board[i][j] == "." :
                               continue
                            elif board[i][j] in seen:
                               return False
                            seen.add(board[i][j])
            return True
         
       if checkRows(board) and checkCol(board) and checkBox(board):
          return True
       else:
          return False
