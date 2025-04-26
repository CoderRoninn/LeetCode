class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        copy = sorted(heights)

        count = 0

        for i in range(len(heights)):
            if heights[i] != copy[i]:
                count += 1
        return count  

        #Time complexity of this algorithm is O(nlogn) because of the sorted funcion which dominates the overall complexity the loop itself is O(n) but sorting is more expensive
        #Space complexity of this algorithm is O(n) because sorted function creates a new list, which stores all element from the orginal list     
        