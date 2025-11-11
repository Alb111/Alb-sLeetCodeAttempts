# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy: ListNode = ListNode()
        tail = dummy
        done_lists: int = 0
        while len(lists) != done_lists:
            done_lists = 0
            local_min: int = 1111
            index_to_add: int = -1
            for i, list_head in enumerate(lists):
                # if list_head is null skip
                if list_head is None:
                    done_lists += 1
                    continue
                # if not null try to find local_min
                if list_head.val < local_min:
                    local_min = list_head.val 
                    index_to_add = i

            # add the local min and get rid of it
            if index_to_add != -1:
                tail.next = lists[index_to_add]
                tail = tail.next
                lists[index_to_add] = lists[index_to_add].next
                
        return dummy.next




