import pytest

from stack import Stack

def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() == True

def test_stack_is_full():
    stack = Stack(size=1)
    stack.push(1)
    assert stack.is_full() == True


def test_stack_push():
    stack = Stack(size=1)
    stack.push(1)
    assert stack.items[0] == 1

def test_stack_pop():
    stack = Stack(size=1)
    stack.push(1)
    assert stack.pop() == 1

def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.pop()

def test_stack_push_full():
    stack = Stack(size=1)
    stack.push(1)
    with pytest.raises(ValueError) :
        stack.push(2)

if __name__ == "__main__":
    pytest.main()