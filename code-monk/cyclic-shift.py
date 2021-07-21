

def cyclic_shift(value: str, k_: str):
    max_ = float("-inf")
    count_ = 0
    rotations = 0
    while count_ < len(value):
        print(count_, value, len(value), max_)
        if max_ < int(value, 2):
            max_ = int(value, 2)
            rotations += 1
        value = value[1:] + value[0]  # shift
        count_ += 1
    return bin(max_), rotations


if __name__ == '__main__':
    num_test_cases = int(input())
    count = 0
    while count < num_test_cases:
        n, k = input().split()
        a = input()
        print(cyclic_shift(a, k))
        count += 1
