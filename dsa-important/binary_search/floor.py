def floor_array(array: list, key):
    left = 0
    right = len(array) - 1
    res = -1
    while left < right:
        mid = (left + right) // 2

        # 3 6 9 45 floor of 7
        if array[mid] == key:
            res = mid

        if array[mid] < key:  # can be a candidate so save the index
            res = mid
            left = mid + 1  # check the same direction

        if array[mid] > key:  # check the opposite side
            right = mid - 1

    return res


if __name__ == '__main__':
    a = [2, 3, 6, 9, 13]
    b = [1, 2, 8, 10, 10, 12, 19]
    index = floor_array(a, 7)
    print(f"index: {index}, value:{a[index]}")

    index = floor_array(b, 9)
    print(f"index: {index}, value:{b[index]}")
