class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # Staircase Method:
        # m, n = len(matrix), len(matrix[0])
        # r,c = 0, n-1

        # while r<m and c>-1:
        #     if matrix[r][c] < target:
        #         r += 1
        #     elif matrix[r][c] > target:
        #         c -= 1
        #     else:
        #         return True
        # return False

        # Binary Search (twice)
        totalRows = len(matrix)
        print(f'totalRows:{totalRows}')

        top = 0
        bottom = totalRows-1
        
        while top <= bottom:
            row = (top+bottom) // 2       
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row -1
            else:
                break

        if not (top <= bottom):
            return False
        


        print(row)
        l=0
        r=len(matrix[row])-1
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] < target:
                l = mid+1
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                return True

        return False
            