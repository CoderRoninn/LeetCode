class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

        #Space complexity of this algorithm takes O(1) because we don't use any additional data structures
        #Time complexity of this algorithm is O(n) because we need to visit each character in the string once to convert lowercase
        