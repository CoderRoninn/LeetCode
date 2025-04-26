class Solution:
    def fib(self, n: int) -> int:

        t1, t2 = 0, 1
        next = None

        if n == 0: #Base case
            return 0

        if n == 1: # Base case
            return 1

        for _ in range(2, n+1):
            next = t1 + t2
            t1 = t2
            t2 = next
        return next   

        #Time complexity of this algorithm is O(n) because we iterate through the loop once where n is the input number
        #The loop runs linearly from 2 to n where n is input number
        #Space complexity of this algorithm is O(1) because we don't use any additional data structure. we only use constant amount of variable    
               
        