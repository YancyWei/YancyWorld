class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int):
        self.stack.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        a = self.stack.pop()
        if self.helper[-1] == a:
            self.helper.pop()
        return a

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(2)
    obj.push(0)
    obj.push(3)
    obj.push(0)
    param_1 = obj.getMin()
    param_2 = obj.pop()
    param_3 = obj.getMin()
    param_4 = obj.pop()
    param_5 = obj.getMin()
    param_6 = obj.pop()
    print([param_1, param_2, param_3, param_4, param_5, param_6])
