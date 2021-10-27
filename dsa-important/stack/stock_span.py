class Stack:
    def __init__(self):
        self.__data = []

    def pop(self):
        self.__data.pop()

    def append(self, inx, val):
        self.__data.append((inx, val))

    def peek(self):
        return self.__data[-1]

    def is_empty(self):
        return len(self.__data) == 0


def sp(stock: list) -> list:
    s = Stack()
    r = []
    i = 0
    while i < len(stock):
        if s.is_empty():
            r.append((-1, None))
            s.append(i, stock[i])

        elif s.peek()[-1] > stock[i]:
            r.append(s.peek())
            s.append(i, stock[i])

        elif s.peek()[-1] <= stock[i]:
            while not s.is_empty() and s.peek()[-1] <= stock[i]:
                s.pop()

            if s.is_empty():
                r.append((-1, None))

            else:
                r.append(s.peek())
                s.append(i, stock[i])

        i += 1
    return r


if __name__ == '__main__':
    a = [100, 80, 60, 70, 60, 75, 85]
    print(a)
    print(sp(a))
    print([ i - v[0] for i, v in enumerate(sp(a))])
