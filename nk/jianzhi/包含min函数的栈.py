class Solution:
    def __init__(self):
        self.stack = []
    def push(self, node):
        # write code here
        return self.stack.append(node)
    def pop(self):
        # write code here
        return self.stack.pop()
    def top(self):
        # write code here
        return self.stack[0]
    def min(self):
        # write code here
        return min(self.stack)