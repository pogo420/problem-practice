# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ptr1 = l1
        ptr2 = l2
        l3 = ListNode()
        ptr3 = l3
        while True:

            if not ptr1:
                ptr1 = ListNode(val=0)
            if not ptr2:
                ptr2 = ListNode(val=0)

            val = (carry + ptr1.val + ptr2.val) % 10
            carry = int((carry + ptr1.val + ptr2.val) / 10)
            print(val)
            ptr3.val = val
            if ptr1.next or ptr2.next:
                ptr3.next = ListNode()
                ptr1 = ptr1.next
                ptr2 = ptr2.next
                ptr3 = ptr3.next
            else:
                if carry != 0:
                    ptr3.next = ListNode(val=carry)
                break

        return l3
