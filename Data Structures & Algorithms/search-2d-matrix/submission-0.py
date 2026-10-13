class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        rows,col = len(matrix), len(matrix[0]) #tells u # of rows, tells 
                                                #u how many col
        L,R = 0, (rows * col) - 1

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
        