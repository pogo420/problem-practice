from link_list_adt import LinkList


def find_intersection(ll1, ll2):
    trav1 = ll1.head.next
    trav2 = ll2.head.next
    i=j=1
    while trav1.next:
        i += 1
        trav1 = trav1.next
    while trav2.next:
        j += 1
        trav2 = trav2.next

    if trav1 != trav2:
        return "No intersection"

    if i == j:
        k = 0
        trav1 = ll1.head.next
        trav2 = ll2.head.next
        while k < i:
            if trav1 == trav2:
                return "intersection", trav1.val
            k += 1
            trav1 = trav1.next
            trav2 = trav2.next
    elif i < j:
        k = 0
        trav1 = ll1.head.next
        trav2 = ll2.head.next
        while k < j-i:
            k += 1
            trav2 = trav2.next
        k = 0
        while k < i:
            if trav1 == trav2:
                return "intersection", trav1.val
            k += 1
            trav1 = trav1.next
            trav2 = trav2.next
    elif i > j:
        k = 0
        trav1 = ll1.head.next
        trav2 = ll2.head.next
        while k < i-j:
            trav1 = trav1.next
            k += 1
        k = 0
        while k < j:
            if trav1 == trav2:
                return "intersection", trav1.val
            k += 1
            trav1 = trav1.next
            trav2 = trav2.next
        return "no intersection"


if __name__ == "__main__":
    l1 = LinkList()
    for i in [3,6,5,9,7,2,1]:
        l1.insert_item(i)
    l2 = LinkList()
    for i in [4, 6]:
        l2.insert_item(i)

    l2.insert_node(l1.find_node(7))

    l1.print_elements()
    l2.print_elements()

    print(find_intersection(l1, l2))
