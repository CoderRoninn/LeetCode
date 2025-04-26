# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, current = None, head

        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node
        return prev    

        #Time complexity of this algorithm is O(n) because we traverse the linked list once where n is the length of input linked list
        #Space completixy of this algortihm is O(1) because we don't use any additional data structures.