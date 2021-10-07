

class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_


def merge_link_list(l1: ListNode, l2:ListNode) -> ListNode:
    head = ListNode()
    curr = head
    temp1 = l1
    temp2 = l2

    while temp1 is not None and temp2 is not None:
        if temp1.val <= temp2.val:
            curr.val = temp1.val
            # curr = temp1  # don't use it will copy the reference
            temp1 = temp1.next_
        else:
            curr.val = temp2.val
            # curr = temp2  # don't use it will copy the reference
            temp2 = temp2.next_

        if temp1 is not None and temp2 is not None:  # prevent creating of last node
            curr.next_ = ListNode()
            curr = curr.next_

    return head


def create_link_list(d) -> ListNode:
    head = ListNode()
    curr = head
    count = 0
    for i in d:
        curr.val = i
        if count < len(d) - 1:
            curr.next_ = ListNode()
            curr = curr.next_
        count += 1

    return head


if __name__ == '__main__':
    d1 = [1, 3, 5, 9, 67]
    d2 = [2, 4, 9, 10, 37]
    l1 = create_link_list(d1)
    l2 = create_link_list(d2)

    l3 = merge_link_list(l1, l2)
    while l3 is not None:
        print(l3.val)
        l3 = l3.next_

