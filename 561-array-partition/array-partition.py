class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        maximized_sum = 0

        nums.sort()

        for i in range(0, len(nums)-1, 2):
            maximized_sum += min(nums[i], nums[i+1])
        return maximized_sum 

        #Time complexity of this algorithm takes O(nlogn) because of sort method.
        #The sort operation dominates the loop, which runs in O(n) time.
        #Space complexity of this algorithm takes O(1) becase we don't use any additional number
        
        