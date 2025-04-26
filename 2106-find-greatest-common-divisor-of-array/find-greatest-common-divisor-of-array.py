class Solution:
    def findGCD(self, nums: List[int]) -> int:

        a, b = min(nums), max(nums)

        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, (a % b)
            return a

        return gcd(a,b)       

        #Time complexity of this algorithm is O(log(min(a,b))) because we divide the numbers repeatedly using modulo
        #Space complexity of this algorithm is O(1) because we don't use any additional data structures
        