import pytest

from basic_data_structure import Stack


def test_empty_stack():
    stack = Stack()
    assert len(stack) == 0


@pytest.mark.parametrize('sequence', (
    [1],
    ['a', 'b', 'c'],
    [object()],
))
def test_inited_stack(sequence: list):
    stack = Stack(*sequence)
    assert len(stack) == len(sequence)


def test_pushed_stack():
    stack = Stack()
    stack.push(0)
    stack.push(1)
    assert len(stack) == 2


def test_mix():
    stack = Stack(1, 2, 3)
    stack.push(4)
    stack.push(5)
    assert len(stack) == 5
