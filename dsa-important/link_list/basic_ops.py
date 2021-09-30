from link_list_implementation import LinkList


def test_create_ll():
    ll = LinkList()
    for i in range(10):
        ll.add(i)

    ll.print_

    reverse_ll(ll)
    ll.print_


def reverse_ll(linkl: LinkList):
    prev = None
    current = linkl.head

    while current is not None:
        next_ = current.next_  # saving next of current
        current.next_ = prev  # current new next is prev
        prev = current  # incrementing prev to current
        current = next_  # incrementing current
    linkl.head = prev  # last element is assigned as head


if __name__ == '__main__':
    test_create_ll()
