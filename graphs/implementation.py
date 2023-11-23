from typing import Dict, List


class Node:
    def __init__(self, id_: int, value: str):
        self.node_id: int = id_
        self.value: str = value


class Graph:

    def __init__(self):
        self.master_data: Dict[int, List[Node]] = {}

    def is_exist(self, n: Node) -> bool:
        if self.master_data.get(n.node_id):
            return True
        else:
            return False

    def add_vertex(self, n: Node):
        self.master_data[n.node_id] = [n]

    def add_edge(self, src: Node, dest: Node):
        source_head = self.master_data.get(src.node_id)
        destination_head = self.master_data.get(dest.node_id)
        source_head.append(destination_head[0])

    def print(self):
        for n in self.master_data:
            for nb in self.master_data.get(n):
                print(nb.node_id, end="--")
            print("\n")


if __name__ == '__main__':
    g = Graph()

    n1 = Node(1, "ola1")
    n2 = Node(2, "ola2")
    n3 = Node(3, "ola3")
    n4 = Node(4, "ola4")
    n5 = Node(5, "ola5")

    g.add_vertex(n1)
    g.add_vertex(n2)
    g.add_vertex(n3)
    g.add_vertex(n4)
    g.add_vertex(n5)

    g.add_edge(n1, n2)
    g.add_edge(n1, n5)
    g.add_edge(n1, n3)

    g.print()
