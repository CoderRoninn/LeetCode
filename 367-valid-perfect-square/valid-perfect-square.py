class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left, right = 1, num

        while left <= right:
            middle = left + (right - left) // 2
            if middle * middle == num:
                return True
            elif middle * middle < num:
                left = middle + 1
            else:
                right = middle - 1
        return False  
        
        #Time complexity of this algorithm is O(logn) because we use binary search to find the square root reducing the search space by half in each iteration
        #Space complexity of this algorithm is O(1) because we don't use any additional data structure

        