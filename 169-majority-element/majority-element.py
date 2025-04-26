from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = Counter(nums)
        return max(freq.items(), key=lambda x: x[1])[0]

       


        #Time complexity of this algorithm is O(n) because we iterate through the input array once to count frequency of each element  where n is the length of imput array
        #Also finding max element takes O(n) where n is the length of imput array
        #Space complexity of this algorithm is O(n) because we created a dictionary(Counter) of length n, where n is the length of input array



        
        