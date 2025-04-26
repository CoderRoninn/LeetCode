import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_heap = [-x for x in nums]   

        heapq.heapify(max_heap) #Takes O(n) on average

        num1 = -heapq.heappop(max_heap) # Takes O(n) on average
        num2 = -heapq.heappop(max_heap)

        return (num1-1) * (num2-1)

        #Time complexity of this algorithm is O(n) # because we iterate through the loop n times to add elements to the heap

        #Space complexity of this algorithm is O(n) because we create a heap of size n where n is the length of input array
        