import pytest

from basic_data_structure import Stack
from basic_data_structure.exceptions import EmptyStackError


def test_init_empty():
    s = Stack()
    s.push(1)
    assert s.pop() == 1


def test_init_not_empty():
    s = Stack(1, 2, 3, 4)
    assert s.pop() == 4


def test_loop():
    s = Stack(1, 2, 3, 4, 5)
    lst = []
    while s:
        lst.append(s.pop())
    assert lst == [5, 4, 3, 2, 1]
    assert len(s) == 0
    assert bool(s) is False


def test_flow():
    s = Stack('a', 'b', 'c', 'd')
    assert len(s) == 4

    s.push('e')
    s.push('f')
    s.push('g')
    assert len(s) == 7

    assert s.pop() == 'g'
    assert len(s) == 6

    assert s.pop() == 'f'
    assert len(s) == 5

    assert s.pop() == 'e'
    assert len(s) == 4

    assert s.pop() == 'd'
    assert len(s) == 3

    assert s.pop() == 'c'
    assert len(s) == 2

    assert s.pop() == 'b'
    assert len(s) == 1

    assert s.pop() == 'a'
    assert len(s) == 0

    with pytest.raises(EmptyStackError):
        s.pop()
    assert len(s) == 0
