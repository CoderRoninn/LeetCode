class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1      

        #Time complexity of this algorithm is O(logn) because we use binary search
        #In each iteration, we halve the search interval by means of binary search
        #Space complexity of this algorithm is O(1) because we only use a constant number of variables.






        