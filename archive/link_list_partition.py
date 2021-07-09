from link_list_adt import LinkList


def partition(head, partition_pivot):
    '''function to implement partition'''
    less_start = None
    less_end = None
    equal_start = None
    equal_end = None
    greater_start = None
    greater_end = None

    trav = head.next

    while trav:

        if trav.val < partition_pivot:
            if not less_start:
                less_start = less_end = trav
            else:
                less_end.next = trav
                less_end = less_end.next

        elif trav.val > partition_pivot:
            if not greater_start:
                greater_start = greater_end = trav
            else:
                greater_end.next = trav
                greater_end = greater_end.next

        else:
            if not equal_start:
                equal_start = equal_end = trav
            else:
                equal_end.next = trav
                equal_end = equal_end.next

        trav = trav.next

    head.next = less_start
    less_end.next = equal_start
    equal_end.next = greater_start
    greater_end.next = None


if __name__ == "__main__":
    ll = LinkList()
    for i in [1, 4, 3, 2, 5, 2, 3]:
        ll.insert_item(i)
    print("before partition")
    ll.print_elements()
    print("-------------------")
    partition(ll.head, 3)
    print("after partition")
    ll.print_elements()
