class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:  #ALL if statements are base cases
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2

        t0, t1, t2 = 0, 1, 1
        next = None

        for _ in range(3, n+1):
            next = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = next
        return next    
       
       #Time complexity of this algorithm is O(n) because we iterate through  the loop once
       #The loop runs from 3 to n where n is input number
       #Space complexity of this algorithm is O(1) because we don't use any additional data strucre. We only used constant amount of variables.

                    