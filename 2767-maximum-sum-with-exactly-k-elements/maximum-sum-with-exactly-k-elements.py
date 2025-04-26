import heapq

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        max_heap = [-number for number in nums]  # This operation takes O(n) on averege because we create a new list of size n

        heapq.heapify(max_heap) # To convert heap takes O(n) on average

        score = 0

        for _ in range(k): # we execute the loop k times so Time complexity is O(k) but total cost depends on what we do inside so total time complexity will be O(k * logn)
            m = -heapq.heappop(max_heap)  # This operation takes O(logn) on avarege
            score += m

            heapq.heappush(max_heap, -(m+1))  # This operation takes O(logn) on avarege

        return score    

        #Time complexity of this algorithm is O(k * logn) where k is the number of operations to execute and n is the number of in the heap(İnput list)
        #Space complexity of this algorithm is O(n) where n is the length of input list



        