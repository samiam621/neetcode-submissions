class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []
        if matrix is None or matrix == []:
            return []

        left,right = 0, len(matrix[0])
        top,bottom = 0, len(matrix)

        if top >= bottom or left >= right:
            return []

        #top row
        for i in range(left,right):
            results.append(matrix[top][i])
        top += 1
        if top < bottom:
            #right
            for i in range(top,bottom):
                results.append(matrix[i][right-1])
            right -= 1

        if top < bottom:
            #bottom 
            for i in range(right-1,left-1,-1):
                results.append(matrix[bottom-1][i])
            bottom -= 1

        if left < right:
            #left
            for i in range(bottom-1, top-1,-1):
                results.append(matrix[i][left])
            left += 1

        sub_matrix = [val[left:right] for val in matrix[top:bottom]]
        results.extend(self.spiralOrder(sub_matrix))
        return results
