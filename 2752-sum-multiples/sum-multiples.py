class Solution:
    def sumOfMultiples(self, n: int) -> int:

        return sum(number for number in range(1, n+1) if number % 3 == 0 or number % 5 == 0 or number % 7 == 0) #Generator expression

        #Time complexity of this algorithm is O(n) beucase we execute the loop n times where n is length of input string
        #Space complexity of this algorithm is O(1) because we don't use any additional data structure
        