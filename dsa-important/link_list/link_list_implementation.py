from typing import Any


class Node:
    def __init__(self, value, nxt):
        self.__value: Any = value
        self.__next: Node = nxt

    @property
    def value(self) -> Any:
        return self.__value

    @property
    def next_(self) -> 'Node':
        return self.__next

    @next_.setter
    def next_(self, nxt):
        self.__next = nxt


class LinkList:

    def __init__(self):
        self.__head = Node(None, None)

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head: Node):
        self.__head = head

    def add(self, val):
        current_node = self.__head

        while True:
            if current_node.next_ is None:
                current_node.next_ = Node(val, None)
                break
            current_node = current_node.next_

    @property
    def print_(self):

        start = self.__head
        temp = start.next_
        while temp is not None:
            print(temp.value)
            temp = temp.next_
        return
