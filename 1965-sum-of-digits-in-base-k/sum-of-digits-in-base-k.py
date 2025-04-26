class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        base_sum = 0

        while n > 0:
            base_sum += n % k
            n = n // k
        return base_sum    
        
        #Time complexity of this algorithm is O(nlogn) because we devide n by k each iteration of the while loop
        #Space complexity of this algorithm is O(1) because we don't use any additional data structures 
        #We only used a fixed number of variables