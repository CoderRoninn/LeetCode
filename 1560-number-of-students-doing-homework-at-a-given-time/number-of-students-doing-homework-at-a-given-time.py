class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        count = 0

        for i in range(len(startTime)):
            if queryTime - startTime[i] >= 0 and endTime[i] - queryTime >= 0:
                count +=1
        return count        


        #Time complexity of this algorithm is O(n) because we iterate through the loop n times, where n is the length of input arrays 
        #Space complexity of this algorithm is O(1) because we don't use any additional data structures only a variable(just a counter variable)