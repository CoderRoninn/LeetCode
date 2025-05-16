from collections import Counter

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        flat_array = [number for rows in nums for number in rows] # To convert 2-D Array to 1-D Array.

        numbers = Counter(flat_array) # To keep values with their frequency in hash-map.

        result = [number for (number, count) in numbers.items() if count == len(nums)] # To find intersection and filter if process.

        return sorted(result)

        #Time complexity of this algorithm is O(n) because we iterate through the array once, where n is the count of elements in 2-D Array
        #Space complexity of this algorithm is O(n) beucase we create a hash-map(Counter) to store frequency of each element.




        
        