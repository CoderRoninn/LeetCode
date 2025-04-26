class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0

        for op in operations:
            if op == "X++" or op == "++X":
                result += 1
            else:
                result -=1
        return result    

        #Time complexity of this algorithm is O(n) because we iterate through the loop n times, where n is the length of given string array
        #Space complexity of this algorithm is O(1) because we don't use any additional data structures we only use a variable         
        