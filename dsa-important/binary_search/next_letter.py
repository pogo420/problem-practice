

def next_letter(arr, key, start, end):
    res = -1
    while start <= end:
        mid = start + (end-start)//2
        print(start, mid, end)
        if mid >= len(arr):
            res = -1
            break

        if arr[mid] == key:
            res = mid + 1
            break

        if ord(arr[mid]) > ord(key):
            res = mid
            end = mid - 1

        else:
            start = mid + 1
    return res


if __name__ == '__main__':
    a = ["a", "c", "f", "j", "m"]
    inx = next_letter(a, "b", 0, len(a))
    print(inx, a[inx])
