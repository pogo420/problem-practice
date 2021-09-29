

def increase_order(n: int):
    # f(n) = f(1-n) print(n)
    if n == 1:  # base condition
        print(n)
        return
    increase_order(n-1)
    print(n)


def decrease_order(n: int):
    # f(n) = print(n) f(n-1)
    if n == 1:  # base condition
        print(n)
        return
    print(n)
    decrease_order(n-1)


if __name__ == '__main__':
    increase_order(5)
    print("---"*10)
    decrease_order(9)
