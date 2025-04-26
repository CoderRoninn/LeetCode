from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)

        return sum(num for (num, count) in freq.items() if count == 1)

        #Time complexity of this algorithm is O(n) because we iterate through the input array once to count of each number
        #Space complexity of this algorithm is O(n) because using Counter we created a dictionary where n is the length of input array

        