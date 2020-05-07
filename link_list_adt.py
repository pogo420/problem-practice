class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
		

class LinkList:

    def __init__(self):
        self.head = Node("*head*")

    def insert_item(self,val):
        trav = self.head
        
        while trav.next:
            trav = trav.next
        trav.next = Node(val)

    def print_elements(self):
        trav = self.head

        while trav:
            print(trav.val)
            trav = trav.next
	
    def find(self, val):
        trav = self.head

        while trav:
            if val == trav.val:
                return True
            trav = trav.next
        return False

    def delete(self, val):
        if not self.find(val):
            return -1
        trav = self.head
        temp = None
        while trav:
             if val == trav.val:
                 temp.next = trav.next

             temp = trav
             trav = trav.next


if __name__ == "__main__":
    ll = LinkList()
    for i in ["a","b","c","d","f"]:
        ll.insert_item(i)

    ll.print_elements()

    print("e",ll.find("e"))
    print("c",ll.find("c"))
    ll.delete("d")
    ll.print_elements()
    print("ola")
    ll.test()
