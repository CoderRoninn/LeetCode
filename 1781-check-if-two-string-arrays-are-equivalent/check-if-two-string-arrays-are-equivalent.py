class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        return "".join(word1) == "".join(word2)

        #Time complexity of this algorithm is O(M+N) because we join all strings in both lists where M and N are the total number of characters in the input lists.


        #Space complexity of this algorithm is O(M+N)  because joining the strings creates two new strings of length M and N          
        