class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []

        for i in range(len(nums)):  #O(n)
            ans.append(nums[i])
        for i in range(len(nums)):  #O(n)
            ans.append(nums[i])
        return ans

        #Time complexity of this algorithm is O(n) because we add every element from input array to ans array twice , where n is the length of input array
        #Space compelxity of this algorithm is O(n) because we created a result array which has 2n elements
       

        #Or we can use merge operation for list 
        #return nums + nums     and time and space complexity of these algorithm is similar to each other  
        