from basic_data_structure import Stack


def test_init_empty():
    stack = Stack()
    stack.push(1)
    assert len(stack) == 1


def test_init_not_empty():
    stack = Stack(1, 2, 3, 4)
    stack.push(5)
    assert len(stack) == 5
    assert stack.pop() == 5


def test_push_twice():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    assert len(stack) == 2
    assert stack.pop() == 'b'
