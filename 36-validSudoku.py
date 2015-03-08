class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        rowDict = dict()
        colDict = dict()
        cellDict = dict()

        row = 0
        col = 0

        result = True
        while row < 9:
            while col < 9:
                currentValue = board[row][col]
                if currentValue != '.':
                    # check row dict
                    tmpRowDict = rowDict.setdefault(row,{})
                    if currentValue not in tmpRowDict:
                        tmpRowDict[currentValue] = True
                    else:
                        return False

                    # check col dict
                    tmpColDict = colDict.setdefault(col,{})
                    if currentValue not in tmpColDict:
                        tmpColDict[currentValue] = True
                    else:
                        return False

                    # check Cell dict
                    cellRow = row/3
                    cellCol = col/3

                    tmpCellDict = cellDict.setdefault((cellRow,cellCol),{})
                    if currentValue not in tmpCellDict:
                        tmpCellDict[currentValue] = True
                    else:
                        return False

                col = col + 1
            col = 0
            row = row + 1

        return result
