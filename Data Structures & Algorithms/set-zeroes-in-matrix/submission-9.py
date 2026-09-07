class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #remember rows and col of each position
        rows,cols = len(matrix), len(matrix[0])
        rowZero = False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    #mark pos for col
                    matrix[0][j]= 0
                    #mark row but one extra var for top row
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
                    
        #set to zero besides first row
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        #[0][0] seperately so no overlap
        if matrix[0][0] == 0:
            #zero the col
            for row in matrix:
                row[0] = 0
        if rowZero:
            #zero the row
            for i in range(cols):
                matrix[0][i] = 0
                    
                    


        
        