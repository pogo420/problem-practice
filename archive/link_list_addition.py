

from link_list_adt import LinkList
result = LinkList()
i = 0

def add_linklist_rev(l1, l2, carry=0):
    #Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
    #Output: 2 -> 1 -> 9. That is, 912.
    trav1 = l1
    trav2 = l2

    if trav1 == None and trav2 == None:
        return

    value = trav1.val + trav2.val + carry
    result.insert_item(value % 10)

    if trav1 != None and trav2 != None:
        add_linklist_rev(
            trav1.next,
            trav2.next,
            0 if value < 10 else 1
        )

    return


def add_linklist(l1, l2):
    #Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
    #Output: 3 -> 0 -> 8. That is, 308.
    trav1 = l1
    trav2 = l2

    if trav1 == None and trav2 == None:
        return 0

    carry = add_linklist(
        trav1.next,
        trav2.next
    )
    value = trav1.val + trav2.val + carry
    temp = value % 10

    result.insert_item_beg(temp)
    global i
    if i > 3 and value > 10:
        result.insert_item_beg(0 if value < 10 else 1)
    i += 1

    return 0 if value < 10 else 1


if __name__ == "__main__":
    l1 = LinkList()
    for i in [7, 1, 6]:
        l1.insert_item(i)
    l2 = LinkList()
    for i in [5, 9, 2]:
        l2.insert_item(i)

    add_linklist(l1.head.next, l2.head.next)
    # add_linklist_rev(l1.head.next, l2.head.next)
    result.print_elements()
