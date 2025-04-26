class Solution:
    def romanToInt(self, s: str) -> int:

        my_dict = {'I':1, 'V':5, 'X':10,   #Fixed size dictionary O(1)
                   'L':50, 'C':100, 'D':500,
                   'M':1000
                   }
        number = 0

        i = 0

        while i < len(s):  # O(n)
            if i+1 <len(s) and my_dict[s[i]] < my_dict[s[i+1]]:
                number += my_dict[s[i+1]] - my_dict[s[i]]
                i += 2
            else:
                number += my_dict[s[i]]
                i += 1    
        return number  

        #Time complexity of this algorithm is O(n) because we execute the loop n times where n is the length input string
        #Space complexity of this algorithm is O(1) because The dictionary is fixed size



                  

        
            
    
   
        