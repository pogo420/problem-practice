from typing import List


def merge(l1: List, l2: List) -> List:
    # merge routine 1
    l = r = 0
    l3 = []

    while l < len(l1) and r < len(l2):
        if l1[l] <= l2[r]:
            l3.append(l1[l])
            l += 1

        elif l1[l] > l2[r]:
            l3.append(l2[r])
            r += 1

    # remaining elements
    while l < len(l1):
        l3.append(l1[l])
        l += 1

    while r < len(l2):
        l3.append(l2[r])
        r += 1

    return l3


def merge_(lt, start, mid, end) -> List:
    # merge routine 2
    # all index are 0 indexed
    l = start
    r = mid+1
    count = 0
    temp = [0]*(end-start+1)

    while l <= mid and r <= end:

        if lt[l] <= lt[r]:
            temp[count] = lt[l]
            l += 1
            count += 1
        else:
            temp[count] = lt[r]
            r += 1
            count += 1

    while l <= mid:
        temp[count] = lt[l]
        l += 1
        count += 1

    while r <= end:
        temp[count] = lt[r]
        r += 1
        count += 1

    for id in range(start, end+1):
        lt[id] = temp[id-start]
    return lt


def merge_recursive(l: List) -> List:
    if len(l) < 2:
        # recursive termination condition
        return l

    middle = len(l) // 2
    s1 = merge_recursive(l[:middle])
    s2 = merge_recursive(l[middle:])
    return merge(s1, s2)


def merge_iterative(l: List) -> List:
    width = 1  # start with 2^0
    n = len(l)
    while width < n:
        left = 0
        while left < n:

            right = min(left + (2 * width) - 1, n-1)

            middle = min(left + width - 1, n - 1)

            merge_(l, left, middle, right)

            left += (width*2)  # hopping based on window
        width *= 2  # growth by power of 2
    return l


if __name__ == '__main__':
    # a = [1, 3, 90, 113]
    # b = [2, 8, 56]
    # ab = [1, 3, 90, 113, 2, 8, 56]
    # print(merge(a, b))
    # print(merge_(ab, 0, 3, 6))
    c = [8, 2, 56, 0, 2, 4, 6, 10, 3, 1]
    print(merge_recursive(c))
    print(merge_iterative(c))
