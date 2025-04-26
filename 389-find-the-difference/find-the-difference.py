class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        sum = 0

        for char in s:
            sum ^= ord(char)

        for char in t:
            sum ^= ord(char)

        return chr(sum)      

       # Time complexity of this algorithm is O(m + n) beucase we iterate through the loops m and times, where m and n are the lengths of the input strings
       # Space complexity of this algorithm is O(1) because we don't use any additional data structures we only use a variable to keep last ascii value


        

        
        