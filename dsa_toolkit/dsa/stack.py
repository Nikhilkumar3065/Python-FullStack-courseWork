class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def is_balanced(self, expression):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in expression:
            if char in pairs.values():
                stack.append(char)

            elif char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False

        return len(stack) == 0