class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        result = []

        i, j = 0, n

        while i < n:
            result.append(nums[i])
            i += 1
            result.append(nums[j])
            j += 1
        return result    

        # Time complexity of this algorithm is O(n) because we iterate through the loop n times, where n is the length of the input array.
        # Space complexity of this algorithm is O(n) because we create a new array of size n, where n is the length of the input array.

        