class Stack:

    def __init__(self):
        self.stack = []
        self.min = None

    def isempty(self):
        return True if len(self.stack) == 0 else False

    def peek(self):
        if self.stack[-1] <= self.min:
            return self.min
        else:
            return self.stack[-1]

    def push(self, value):
        if self.isempty():
            self.stack.append(value)
            self.min = value

        elif value >= self.min:
            self.stack.append(value)

        elif value < self.min:
            self.stack.append(2*value-self.min)
            self.min = value
        return

    def pop(self):
        temp = None
        if self.stack[-1] <= self.min:
            temp = self.min
            self.min = (temp*2)-(self.stack[-1])  # setting minimum
        else:
            temp = self.stack[-1]
        self.stack.pop()


if __name__ == "__main__":
    t = Stack()
    for i in [5,6,3,7,1,9]:
        t.push(i)

    while t.stack:
        print("peek",t.peek())
        print("min",t.min)
        t.pop()
        print("-"*10)
