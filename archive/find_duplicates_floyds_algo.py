

def find_duplicate(arr):
    i = arr[0]  # assigning the head
    j = arr[0]  # assigning the head
    while True:
        i = arr[i]  # x speed
        j = arr[arr[j]]  # 2x speed
        if i == j:  # duplicate or loops
            break

    ptr1 = arr[0]  # beginning
    ptr2 = j  # point of meet

    while ptr1 != ptr2:  # next match
        ptr1 = arr[ptr1]  # same speed
        ptr2 = arr[ptr2]

    print(ptr1)


a = [3,4,1,2,2]
find_duplicate(a)
