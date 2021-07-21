def shift(value: str):
    return value[1:] + value[0]


def get_max(value: str) -> str:
    max_ = float("-inf")
    count_ = 0
    while count_ < len(value):
        if max_ < int(value, 2):
            max_ = int(value, 2)
        value = shift(value)  # shift
        count_ += 1
    return bin(max_)[2:]


def cyclic_shift(value: str, k_: str):
    max_bin = get_max(value)
    return max_bin


if __name__ == '__main__':
    num_test_cases = int(input())
    count = 0
    while count < num_test_cases:
        n, k = input().split()
        a = input()
        print(cyclic_shift(a, k))
        count += 1
