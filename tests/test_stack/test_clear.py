import pytest

from basic_data_structure import Stack
from basic_data_structure.exceptions.stack_exceptions import StackIsEmptyError


def test_with_init():
    stack = Stack(1, 2, 3)
    stack.clear()
    assert bool(stack) is False
    assert len(stack) == 0
    with pytest.raises(StackIsEmptyError):
        stack.pop()


def test_with_push():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.clear()
    assert bool(stack) is False
    assert len(stack) == 0
    with pytest.raises(StackIsEmptyError):
        stack.pop()
