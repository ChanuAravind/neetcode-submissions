class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        box_set = [[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            seen=set()
            column_seen = set()
            
            # row check
            for j in range(9):
                if board[i][j] == '.':
                    continue
                    
                elif board[i][j] in seen:
                    return False
                seen.add(board[i][j])
                
            for k in range(9):
                if board[k][i] == '.':
                    continue
                elif board[k][i] in column_seen:
                    return False
                column_seen.add(board[k][i])

            for l in range(9):
                if board[i][l] == '.':
                    continue
                elif board[i][l] in box_set[i//3][l//3]:
                    return False
                box_set[i//3][l//3].add(board[i][l])
        return True