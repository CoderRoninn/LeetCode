class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_double_digit, sum_single_digit = 0, 0

        for number in nums:
            if number <= 9:
                sum_single_digit += number
            else:
                sum_double_digit += number

        return sum_single_digit != sum_double_digit   



        #Space complexity of this algorithm is O(1) because we don't use any additional data structure
        #Time complexity of this algorithm is O(n) because we iterate through  the loop n times where n is the length of input array         


        