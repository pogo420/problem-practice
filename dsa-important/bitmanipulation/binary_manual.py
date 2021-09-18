# binary addition: 1+0=1; 1+1=10
# binary subtraction: using 2's complement.
# 2's complement: inverse all bit + 1
# xor: returns 1 when bits are different. Else 0
# Right shift: >> n; equivalent to div by 2^n
# Left shift: << n; equivalent to mul by 2^n
# even: number & 1 = 0

def get_binary(decimal_: int) -> str:
    """
    get binary string
    """
    return bin(decimal_)[2:]


def swap_numbers(a: int, b: int):
    """Three times xor operations"""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)


if __name__ == '__main__':
    print(get_binary(88))
    swap_numbers(5, 9)
