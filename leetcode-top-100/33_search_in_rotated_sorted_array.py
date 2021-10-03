# pivot is an element which will change the order of sorting

def find_pivot(data, left, right) -> int:
    mid = left // 2 + right // 2
    if data[mid] > data[mid + 1]:
        return mid + 1

    if data[left] < data[mid]:  # first half is increasing, check second half for pivot
        return find_pivot(data, mid + 1, right)

    else:  # check first half for pivot
        return find_pivot(data, left, mid - 1)


if __name__ == '__main__':
    d = [9, 12, 15, 17, 25, 28, 32, 37, 3, 5, 7, 8]
    pivot_index = find_pivot(d, 0, len(d))
    print(f"index: {pivot_index}, value: {d[pivot_index]}")
