#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(not(list1 or list2)):
            return

        #pointers to go through list1 and list2
        p1=list1
        p2=list2
                
        #output and dummy node
        output = ListNode()
        dummy = output
        
        while(p1 or p2):
            if not p1:
                dummy.next = p2
                dummy = dummy.next
                p2 = p2.next

            elif not p2:
                dummy.next = p1
                dummy = dummy.next
                p1 = p1.next

            elif(p1.val < p2.val):
                dummy.next = p1
                dummy = dummy.next
                p1 = p1.next

            elif(p1.val > p2.val):
                dummy.next = p2
                dummy = dummy.next
                p2 = p2.next

            else:
                dummy.next = p1
                dummy = dummy.next
                p1 = p1.next
                dummy.next = p2
                dummy = dummy.next
                p2 = p2.next
                
        return output.next


# @lc code=end

