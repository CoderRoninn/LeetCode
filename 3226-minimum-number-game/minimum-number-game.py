class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        arr = []  # o(1) space complexity because it is empty

        nums.sort() # Sort the array from smaller to bigger takes O(nlogn)

        for i in range(0, len(nums), 2):  #O(n) we execute the loop n / 2 times 
            alice_movement = nums[i]
            bob_movement = nums[i+1]

            arr.append(bob_movement) #O The append() method runs in O(1) time on average.
            arr.append(alice_movement) #O(1)
        return arr    

        #Time complexity of this algorithm is O(nlogn) because the sorting dominates
        #Space complexity of this algorithm is O(n) because output list and sorting use O(n) memory
        