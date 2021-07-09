from stack_adt import Stack


def stack_sort(s_original, s_temp):

    while not s_original.isempty():
        temp = s_original.pop()
        if s_temp.isempty():
            s_temp.push(temp)
            continue
        while (not s_temp.isempty()) and temp < s_temp.peek():
            s_original.push(s_temp.pop())
        s_temp.push(temp)

    return s_temp


if __name__ == "__main__":
    # arr = [1, 8, 2, 5]
    arr = [9, 8, 2, 5]
    s1 = Stack()
    s2 = Stack()
    for i in arr:
        s1.push(i)

    print(stack_sort(s1, s2).stack)
