from typing import List
# Time complexity O(nlogn)
# Space complexity O(N)


def merge(l1: List, l2: List) -> List:
    # merge routine
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


def merge_recursive(l: List) -> List:
    if len(l) < 2:
        # recursive termination condition
        return l

    middle = len(l) // 2
    s1 = merge_recursive(l[:middle])
    s2 = merge_recursive(l[middle:])
    return merge(s1, s2)


if __name__ == '__main__':
    # a = [1, 3, 90, 113]
    # b = [2, 8, 56]
    # ab = [1, 3, 90, 113, 2, 8, 56]
    # print(merge(a, b))
    # print(merge_(ab, 0, 3, 6))
    c = [8, 2, 56, 0, 2, 4, 6, 10, 3, 1]
    print(merge_recursive(c))
