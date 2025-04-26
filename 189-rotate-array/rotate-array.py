class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        def rotate_array(a: int, b: int) -> None:
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
        rotate_array(0, len(nums)-1) #O(n)
        rotate_array(0, k-1) #O(n)
        rotate_array(k, len(nums)-1)  #O(n) 

        # Time complexity of this algorithm is O(n) we reverse the array 3 times reverse, each reverse operation takes O(n) linear time, where n is the length of input array
        # Space complexity of this algorithm is O(1) because we don't use any additonal data structures; we only modify the array in-place
       
        