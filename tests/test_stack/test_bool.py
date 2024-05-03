from basic_data_structure import Stack


def test_empty_stack():
    stack = Stack()
    assert bool(stack) is False


def test_inited_stack():
    stack = Stack('a')
    assert bool(stack) is True


def test_pushed_stack():
    stack = Stack()
    stack.push(0)
    assert bool(stack) is True


def test_mix():
    stack = Stack(1, 2, 3)
    stack.push(4)
    stack.push(5)
    assert bool(stack) is True


def test_clear():
    stack = Stack(1, 2, 3)
    stack.push(4)
    stack.push(5)
    stack.clear()
    assert bool(stack) is False
