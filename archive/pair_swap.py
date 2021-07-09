def pair_swap(n):

    even_mask = 0xaaaaaaaa
    odd_mask = 0x55555555

    return ((n & even_mask)>>1 | (n & odd_mask) <<1)



print(pair_swap(23))
