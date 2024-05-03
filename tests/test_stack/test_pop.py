import pytest

from basic_data_structure import Stack
from basic_data_structure.exceptions.stack_exceptions import StackIsEmptyError


def test_init_empty():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1


def test_init_not_empty():
    stack = Stack(1, 2, 3, 4)
    assert stack.pop() == 4


def test_loop():
    stack = Stack(1, 2, 3, 4, 5)
    lst = []
    while stack:
        lst.append(stack.pop())
    assert lst == [5, 4, 3, 2, 1]
    assert len(stack) == 0
    assert bool(stack) is False


def test_flow():
    stack = Stack('a', 'b', 'c', 'd')
    assert len(stack) == 4

    stack.push('e')
    stack.push('f')
    stack.push('g')
    assert len(stack) == 7

    assert stack.pop() == 'g'
    assert len(stack) == 6

    assert stack.pop() == 'f'
    assert len(stack) == 5

    assert stack.pop() == 'e'
    assert len(stack) == 4

    assert stack.pop() == 'd'
    assert len(stack) == 3

    assert stack.pop() == 'c'
    assert len(stack) == 2

    assert stack.pop() == 'b'
    assert len(stack) == 1

    assert stack.pop() == 'a'
    assert len(stack) == 0

    with pytest.raises(StackIsEmptyError):
        stack.pop()
    assert len(stack) == 0
