class Solution:
    def countSeniors(self, details: List[str]) -> int:

        count = 0

        m = len(details) 

        for i in range(m): # İt takes O(n) on average
            age = int(details[i][11:13])
            if age > 60: #it takes O(1) because it is a simple process
                count += 1
        return count        

        #Time complexity of this algorithm takes O(n) where n is the length input string
        #Space complexity of this algorithm takes O(1) because we don't use any addtional data structure 
        