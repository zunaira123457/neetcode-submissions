class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix), len(matrix[0])

        L,R = 0, (row * col) - 1

        while L <= R: 
            mid = (L + R) // 2
            mid_val = matrix[mid // col][mid % col]
            if mid_val < target: 
                L = mid + 1
            elif mid_val > target: 
                R = mid - 1
            else: 
                return True
        return False
        