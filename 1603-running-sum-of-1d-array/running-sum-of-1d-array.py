class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        runnig_sum = []

        for number in nums:
            sum += number
            runnig_sum.append(sum)

        return runnig_sum   

        #Time complexity of this algorithm is O(n) because we iterate through the loop n times, where n is the length of the input array
        #Space complexity of this algorithm is O(n) because we create an empty list and  add n elements into it, where n is the length of the input array 


        