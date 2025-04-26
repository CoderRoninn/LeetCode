class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 2
        next = None

        if n == 1:
            return 1

        if n == 2:
            return 2

        for _ in range(2,n):
            next = prev1 + prev2
            prev1 = prev2
            prev2 = next

        return next   

        #Time complexity of this algorithm is O(n) because we iterate thought the loop once 
        #The loop runs from 2 to n  where n is input number
        #Time space complexity  of this algoirthm is O(1) because we don't use any additional data structure. we used only constant amount variable 

                
        

        