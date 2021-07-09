def get_next(n):
    print("n:",bin(n))

    c = n
    c0 = 0
    c1 = 0

    while ((c&1) == 0 and c!=0):
        c0 += 1
        c >>= 1

    while (c&1):
        c1 += 1
        c >>= 1

    p = c0+c1
    print("p pos of non trailing zero:",p)

    n |= (1 << p)
    print("n after flip 7th bit",bin(n))

    n &= ~((1 << p)-1)
    print("n after clearning all bits after p", bin(n))

    n |= ((1<<(c1-1))-1)
    print("inserting c1-1 rows",bin(n))
    print(n)


def get_prev(n):
    print("n:",bin(n))

    c = n
    c0 = 0
    c1 = 0

    while (c&1):
        c1 += 1
        c >>= 1


    while ((c&1) == 0 and c!=0):
        c0 += 1
        c >>= 1


    p = c0+c1
    print("p pos of non trailing one:",p)


    n &= ~((1<<(p+1))-1)
    print("n after clearning all bits including  p till LSB", bin(n))


    print("adding c1+1 ones immediately after p followed by c0-1 zeros")

    n |= ((1<<(c1+1))-1)<<(c0-1)
    print("n", bin(n))
    print(n)



#n = 8
n = 13967
#get_next(n)
get_prev(n)
