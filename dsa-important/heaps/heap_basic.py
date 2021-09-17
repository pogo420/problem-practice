# Heap
# Complete Binary tree.
# At most 2 elements.
# Data is filled from left to right
# Max Heap: Parent is >= children
# Min Heap: Parent is <= children
# Heap is mostly implemented by array.
# Heapify: Technique to convert to heap O(n)
# Delete heap-> deleting root , O(logn)
# Insert heap-> insert an element at the end , O(logn)
# Heap sort: O(nlogn)


def swap(array: list, index_1: int, index_2: int):
    """Swap function"""
    temp = array[index_2]
    array[index_2] = array[index_1]
    array[index_1] = temp


def heapify(data_list: list, parent: int):
    """implementing heapify algorithm
        1. Find max/min of children.
        2. swap the max/min with the parent data.
        3. Run the logic for new swapped children.
    """
    largest = parent
    left = parent * 2 + 1
    right = parent * 2 + 2

    if left < len(data_list) and data_list[left] > data_list[largest]:
        largest = left

    if right < len(data_list) and data_list[right] > data_list[largest]:
        largest = right

    if largest != parent:
        swap(data_list, parent, largest)
        heapify(data_list, largest)


def create_heap(data: list):
    """
    1. Start from non leaf node end to root
    2. Do heapify every iteration.
    """
    non_leaf_end = len(data) // 2

    current_node = non_leaf_end
    while current_node >= 0:
        heapify(data, current_node)
        current_node -= 1

    return data


def delete_heap(data: list) -> list:
    """
    1. Replace root node with last element
    2. Run heapify on the root.
    """
    data[0] = data[-1]
    data = data[:-1]
    heapify(data, 0)

    return data


def insert_heap(data_list: list, element):
    """
    1. parent and node comparison.
    2. Move level up to next parent.
    """
    data_list.append(element)  # adding at the end.
    current_index = len(data_list) - 1  # start from end.
    while current_index > 0:
        parent = (current_index//2) - 1  # calculating parent.
        if data_list[parent] < data_list[current_index]:
            swap(data_list, parent, current_index)
            current_index = parent
        else:
            return data_list
    return data_list


def heap_sort():
    """
    1. create heap
    2. delete root
    Complexity: O(n + nlogn) = O(n)
    """
    pass


if __name__ == '__main__':
    data = [1, 4, 3, 7, 8, 9, 10]
    print(create_heap(data))
    valid_heap = [10, 8, 9, 7, 4, 1, 3]
    print(delete_heap(valid_heap))

    valid_heap = [10, 8, 9, 7, 4, 1, 3]
    print(insert_heap(valid_heap, 12))

#    10
#  8   9
# 7 4 1 3
# 6