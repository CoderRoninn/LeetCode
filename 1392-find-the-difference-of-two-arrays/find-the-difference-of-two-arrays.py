class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        answer = []
        temp = []

        set1 = set(nums1) # İt takes O(m) on average where m is the length of nums1
        set2 = set(nums2) # It itakes O(n) on average where n is the length of nums2

        for number in set1: # İt takes O(m) on average
            if number not in set2: 
                temp.append(number) # It normally takes O(1) but we do this operation for m times so O(m)

        answer.append(temp)

        temp2 = []

        for number in set2:
            if number not in set1:
                temp2.append(number)   

        answer.append(temp2)
        return answer

        #Time complexity of this algorithm is  O(m + n) because we execute the loop over both sets once
        #Space complexity of this algorithm is O(m + n) because we convert lists to set where m is the length of nums1 and  n is the length of nums2

        # Or We can use the set difference operation.

        """
        set1, set2 = set(nums1), set(nums2)
        
        diff1, diff2 = list(set1 - set2), list(set2 - set1)

        return [diff1, diff2]
        """

          

                

        