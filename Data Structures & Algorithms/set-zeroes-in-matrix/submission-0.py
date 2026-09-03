class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #remember rows and col of each position
        mark_set=set()

        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    mark_set.add((i,j))
        for i,j in mark_set:
            matrix[i] = [0] * len(matrix[i])
            for row in matrix:
                row[j] = 0
               
        