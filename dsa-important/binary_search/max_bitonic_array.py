

def max_bitonic(d: list):

    start = 0
    end = len(d) - 1

    while start <= end:
        mid = start + (end-start)//2

        if mid < len(d) - 1 and d[mid] > d[mid+1]:
            return mid

        if d[mid] > start:
            start = mid+1
        else:
            end = mid-1


if __name__ == '__main__':
    a = [1, 20, 33, 84, 60, 45, 21]
    i = max_bitonic(a)
    print(f"{i}, value: {a[i]}")
