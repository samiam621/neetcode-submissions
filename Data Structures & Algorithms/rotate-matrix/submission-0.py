class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l,r = 0, len(matrix)-1
        #move onto next rotation
        while l<r:
            #rotation
            for i in range(r-l):
                top,bottom = l,r #still 0,2
                #save 
                topLeft = matrix[top][l+i]
                
                #top right becomes top left
                matrix[top][l+i] = matrix[bottom-i][l] 
                matrix[bottom-i][l]=matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft

            l += 1
            r -= 1



        