class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    count += 1
            result.append(count)
        return result

        # Time complexity of this algorithm is O(n^2), becasue we iterate through the loop n-1 times for each element.
        # It is a brute force algorithm
        # Space complexity of this algorithm is O(n), because we create a result list of size n to store the count of smaller elements for each element.