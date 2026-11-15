class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict={}
        colDict={}
        subBoxDict={}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    index = (i//3,j//3)
                    if index in subBoxDict:
                        tempRow = subBoxDict[index]
                        if board[i][j] in tempRow:
                            return False
                        tempRow.append(board[i][j])
                        subBoxDict[index] = tempRow
                    else:
                        subBoxDict[index] = [board[i][j]]

                    if i in rowDict:
                        tempRow = rowDict[i]
                        if board[i][j] in tempRow:
                            return False
                        tempRow.append(board[i][j])
                        rowDict[i] = tempRow
                    else:
                        rowDict[i] = [board[i][j]]

                    if j in colDict:
                        tempCol = colDict[j]
                        if board[i][j] in tempCol:
                            return False
                        tempCol.append(board[i][j])
                        colDict[j] = tempCol
                    else:
                        colDict[j] = [board[i][j]]
        return True



        