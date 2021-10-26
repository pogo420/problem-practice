


def count_subset_sum_diff(a, target, n):
    if target == 0:
        return 1  # empty set

    if n == 0 and target > 0:
        return 0  # no elements and +ve target

    if a[n-1] <= target:
        return count_subset_sum_diff(a, target - a[n-1], n - 1) + count_subset_sum_diff(a, target, n - 1)

    else:
        return count_subset_sum_diff(a, target, n - 1)


if __name__ == '__main__':
    a_ = [1, 1, 2, 3]
    diff = 3
    tar_ = (sum(a_) + diff) / 2
    print(tar_)
    print(count_subset_sum_diff(a_, tar_, len(a_)))
