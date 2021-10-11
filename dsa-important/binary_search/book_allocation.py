

def valid_partition(a, max_, k):
    if k > len(a):
        return False

    partition = 1
    sum = 0

    for i in a:
        # print(i, sum, partition, max_)
        sum += i
        if sum > max_:
            sum = i
            partition += 1

    if partition > k:
        return False
    elif partition == k:
        return True
    else:
        return False


def book_allocation(array, k):

    start = max(array)
    end = sum(array)
    res = -1
    while start <= end:
        mid = start + (end - start)//2

        if valid_partition(array, mid, k):
            res = mid
            end = mid - 1

        else:
            start = mid + 1

    return res


if __name__ == '__main__':
    ar = [10, 20, 30, 40]
    print(book_allocation(ar, 2))

    # print(valid_partition(ar, 75, 2))