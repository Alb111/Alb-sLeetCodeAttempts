class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return head

        curr: Node = head
        newNode: Node = None
        old_to_new: dict[Node, Node] = {}

        # make a copy of all nodes and hash them
        while curr:
            newNode = Node(curr.val, None, None)
            old_to_new[curr] = newNode
            curr = curr.next

        # now connect these nodes
        new_head = old_to_new[head]
        curr = head
        new_curr: Node = new_head

        while curr:
            if curr.next:
                new_curr.next = old_to_new[curr.next]
            else:
                new_curr.next = None
                
            if curr.random:
                new_curr.random = old_to_new[curr.random]
            else:
                new_curr.random = None

            curr = curr.next
            new_curr = new_curr.next

        return new_head
            
        
