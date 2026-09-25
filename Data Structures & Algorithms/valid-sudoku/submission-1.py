class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        #have for loops that check value in row then check if its in the col. if it is return false, if not then true and make sure to add that vlue to the rows/col to make sure hwen ur checking for hte next one, its in teh arrya 
        #range(9) gives you the numbers 0 through 8. Using them as row/column indices, you touch every one of the 9 × 9 = 81 cells.board is 9×9
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": #A "." means empty cell. Empty cells don't need any duplicate check.
                    continue
                if val in rows[r] or val in cols[c] or val in square[(r//3, c//3)]:
                    return False 
                rows[r].add(val)
                cols[c].add(val)
                square[(r//3, c//3)].add(val)
        return True

#r // 3 which row-band (0, 1, or 2) c // 3 which column-band (0, 1, or 2) (r//3, c//3) tuple uniquely identifying one of the 9 boxes square[...] the set for that box (auto-created by defaultdict) .add(val) record this digit as "seen in this box"