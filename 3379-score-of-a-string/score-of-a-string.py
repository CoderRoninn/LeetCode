class Solution:
    def scoreOfString(self, s: str) -> int:

        return sum( abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) -1 ) ) #Generator expression

        

        #We used abs() function to get the absolute value of subtraction
        #We used ord() function to get ASCII value of each charecter
        #Time complexity of this algorithm is O(n), because we execute the loop n times where n is length of the input string
        #Space complexity of this algorithm is O(1) because we don't use any additional data structure
        