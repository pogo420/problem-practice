def min_flips(a, b):
    temp = (a^b)
    count = 0
    while temp:
        temp &= (temp-1)
        count += 1

    return count



print(min_flips(29, 15))
