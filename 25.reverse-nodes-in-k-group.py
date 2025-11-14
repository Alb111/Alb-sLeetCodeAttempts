# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # check size of the list
        curr: ListNode = head
        leng: int = 0
        while curr:
            curr = curr.next
            leng += 1

        if leng < k:
            return head

        tail: ListNode = head                
        tail_prev: ListNode = None               
        out: ListNode = None
        temp: ListNode = None
        prev: ListNode = None

        i: int = 0
        while i + k <= leng:
            curr = tail
            prev = None
            # chunk reverse
            for y in range(k):    
                #print(curr.val)
                i += 1
                temp = curr.next
                curr.next = prev                    
                prev = curr
                curr = temp

            start = prev
            if out is None:
                out = start
            
            print(tail.val)
            if tail_prev is not None:
                tail_prev.next = start

            tail_prev = tail
            tail = curr
    
        if leng % k != 0:
            tail_prev.next = tail
        
        return out 




