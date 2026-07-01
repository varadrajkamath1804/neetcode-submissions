class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        column=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num==".":
                    continue
                
                b=(r//3)*3+(c//3)
                if num in row[r]:
                    return False
                if num in column[c]:
                    return False
                if num in box[b]:
                    return False
                
                row[r].add(num)
                column[c].add(num)
                box[b].add(num)
        return True




                
        