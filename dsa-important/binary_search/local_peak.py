
def peak(n: list):
    start = 0
    end = len(n) - 1
    res = -1
    while start <= end:
        mid = start + (end- start)//2

        if 0 < mid < len(n) - 1 \
                and n[mid] > n[mid + 1] \
                and n[mid] > n[mid - 1]:
            res = mid
            break

        if mid == 0 and n[mid] > n[mid + 1]:
            res = mid
            break

        if mid == len(n) - 1 and n[mid] > n[mid - 1]:
            res = mid
            break

        if n[mid] < n[mid + 1]:
            start = mid + 1

        elif n[mid] < n[mid - 1]:
            end = mid - 1

    return res


if __name__ == '__main__':
    n = [12, 3, 2, 4, 9, 7]
    i = peak(n)
    print(f"{i} value: {n[i]}")

