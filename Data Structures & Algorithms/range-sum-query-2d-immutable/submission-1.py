class NumMatrix:
    #BETTER 

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        row  = len(matrix)
        col = len(matrix[0])
        self.prefix = [[0]*(col+1) for i in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                self.prefix[i][j] = (
                    matrix[i-1][j-1]
                    + self.prefix[i-1][j]
                    + self.prefix[i][j-1]
                    - self.prefix[i-1][j-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2+1][col2+1]
        left = self.prefix[row2+1][col1]
        top = self.prefix[row1][col2+1]
        overlap = self.prefix[row1][col1]
        ans = total - left - top + overlap
        return ans



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)