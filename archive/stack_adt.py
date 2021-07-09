class Stack:

    def __init__(self):
        self.stack = []

    def isempty(self):
        return True if len(self.stack) == 0 else False

    def peek(self):
        return self.stack[-1]

    def push(self, value):
        self.stack.append(value)
        return

    def pop(self):
        return self.stack.pop()


if __name__ == "__main__":
    t = Stack()
    for i in [5,6,3,7,1,9]:
        t.push(i)

    print(t.pop())
