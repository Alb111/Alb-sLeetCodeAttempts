# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # outs of each stage
        add_carry: int = 0
        add_sum: int = 0

        # total sum carrying sum of all stages
        total_sum: ListNode = ListNode(1)
        
        # while to loop through each stage
        curr1: ListNode = l1
        curr2: ListNode = l2

        # Construct a List along the way
        curr3: ListNode = total_sum

        while curr1 and curr2:
            # find sum of curr stage and add it to the list
            add_sum = (curr1.val + curr2.val + add_carry) % 10
            curr3.next = ListNode(add_sum, None)
                      
            # get carry for next stage
            add_carry = (curr1.val + curr2.val + add_carry) // 10

            # move dummy nodes
            curr1 = curr1.next
            curr2 = curr2.next
            curr3 = curr3.next

        # if l1 or l2 is bigger we have to process that as well
        rest_of_list: ListNode = curr1 if (curr1 is not None) else curr2

        while rest_of_list: 
            # find sum of stage
            add_sum = (rest_of_list.val + add_carry) % 10
            curr3.next = ListNode(add_sum, None)

            add_carry = (rest_of_list.val + add_carry) // 10

            # move dummies
            rest_of_list = rest_of_list.next
            curr3 = curr3.next

        # handle overflow
        if add_carry:
            curr3.next = ListNode(1, None)


        return total_sum.next
           
