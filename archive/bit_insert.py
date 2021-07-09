# insert m in n from i to j bits in n
# 

def bit_insert(n, m, i, j):
    allone = 255
    left = allone << (j+1)
    right = (1<<i)-1
    mask = left | right
    print(bin(allone))
    print(bin(left))
    print(bin(right))
    print(bin(mask))
    print(bin(n&mask))
    print(bin(m<<i))
    print(bin((n&mask)|(m<<i))) 

bit_insert(1,2,2,4)
