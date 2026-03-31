class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            box_set = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])

                if board[j][i] != "." and board[j][i]  in col_set:
                    return False
                col_set.add(board[j][i])
                
                if board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] != "." and board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] in box_set: return False
                box_set.add(board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3])

        return True

            