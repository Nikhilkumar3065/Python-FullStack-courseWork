from dsa.stack import Stack
def test_stack_push_pop():
    stack = Stack()
    stack.push(10)
    assert stack.pop() == 10