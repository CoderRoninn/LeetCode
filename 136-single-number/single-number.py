class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        single = 0

        for num in nums:
            single ^= num

        return single

        #Time complexity of this algoirthm is O(n) because we itarete through  the loop once
        #The loop runs n times where n is the length of input array
        #Space complexity of this algorithm is O(1) because we don't use any additional data structure            