class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        

    def push(self, val):
        self.stack.append(val)
        if not self.mini or val <= self.mini[-1]:
            self.mini.append(val)
        

    def pop(self):
        popped = self.stack.pop()
        if popped == self.mini[-1]:
            self.mini.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.mini[-1]