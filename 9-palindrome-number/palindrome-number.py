class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        original_number = x

        if x < 0:
            x = -x

        calculated_number = 0

        while x > 0:
            calculated_number = 10 * calculated_number + (x % 10)
            x //= 10  

        return original_number == calculated_number  

        #Space complexity of this algorithm is O(1) because we don't use any additional data structures
        #Time complexity of this algorithm is O(logn) because we divide x by 10 in each iteration of the while loop, which reduces the number of digits logarithmically 
        