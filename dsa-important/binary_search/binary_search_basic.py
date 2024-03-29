

def bs(arr, start, end, key):
    mid = (start + end)//2

    if start > end or mid >= len(arr):  # edge cases shield
        return -1

    if arr[mid] == key:
        return mid

    if arr[mid] > key:
        return bs(arr, start, mid-1, key)

    else:
        return bs(arr, mid+1, end, key)


def bs_iterative(arr, start, end, key):

    while start <= end:
        mid = (start + end) // 2

        if mid >= len(arr):  # edge cases shield
            return -1

        if arr[mid] == key:
            return mid

        if arr[mid] > key:
            end = mid - 1

        else:
            start = mid + 1

    return -1


if __name__ == '__main__':
    a = [1, 3, 5, 7, 9, 10]
    print(bs(a, 0, len(a), 56))
    print(bs(a, 0, len(a), -8))
    print(bs(a, 0, len(a), 4))
    print(bs(a, 0, len(a), 9))

    print(bs_iterative(a, 0, len(a), 56))
    print(bs_iterative(a, 0, len(a), -8))
    print(bs_iterative(a, 0, len(a), 4))
    print(bs_iterative(a, 0, len(a), 9))
