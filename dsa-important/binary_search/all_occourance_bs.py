

def bs(arr, start, end, key, result):
    mid = (start + end)//2

    if start > end or mid >= len(arr):  # edge cases shield
        return -1

    if arr[mid] == key:  # when ever matching check both sides
        result.append(mid)
        bs(arr, start, mid-1, key, result)
        bs(arr, mid + 1, end, key, result)
        return

    if arr[mid] > key:
        return bs(arr, start, mid-1, key, result)

    else:
        return bs(arr, mid+1, end, key, result)


if __name__ == '__main__':
    a = [1, 3, 5, 7, 7, 9, 10]
    result = []
    bs(a, 0, len(a), 56, result)
    print(result)

    result = []
    bs(a, 0, len(a), -8, result)
    print(result)

    result = []
    bs(a, 0, len(a), 4, result)
    print(result)

    result = []
    bs(a, 0, len(a), 7, result)
    print(result)
