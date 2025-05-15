class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        pascal_triangle = []
        
        for i in range(rowIndex+1):
            values = [1] * (i+1)
            for j in range(1,i):
                values[j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
            pascal_triangle.append(values)
        return pascal_triangle[rowIndex]      

        #Time complexity of this algorithm is O(n^2) beucase we iterate through the each row 
        #Also it is a dynamic progrraming problem
        #Space complexity of this algorithm is O(n^2) because we create a pascal triangle as a 2-D list  
        