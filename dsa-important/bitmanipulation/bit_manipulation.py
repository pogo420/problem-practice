# ith bit ? Create mask 1<<i if number & mask == 0 then ith bit is 0
# set ith bit ? Create mask 1<<i  and do  number | mask
# clear ith bit ? Create mask ~(1<<i)  and do  number & mask
# number of bits(0 and 1) in a binary number n is logn + 1 (base: 2)
# number of digits  a decimal number n is logn + 1 (base: 10)
# number of bits to change for a -> b: DO xor to get changed bits. Count set bits.


def cal_setbits(n: int):
    """Log n complexity"""
    count = 0
    while n != 0:
        if n & 1:
            count += 1
        n >>= 1
    return count


def cal_setbits_opti(n: int):
    """n & n-1 clears the LSB(left most) of n
       algorithm runs for # of set bits
       1101 count: 1
       1100 count: 2
       1000 count: 3
       0000
    """
    count = 0
    while n:
        n = n & (n-1)
        count += 1
    return count


if __name__ == '__main__':
    print(cal_setbits(13))
    print(cal_setbits_opti(13))
