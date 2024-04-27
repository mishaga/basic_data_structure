import pytest

from basic_data_structure import Stack
from basic_data_structure.exceptions import EmptyStackError


def test_with_init():
    s = Stack(1, 2, 3)
    s.clear()
    assert bool(s) is False
    assert len(s) == 0
    with pytest.raises(EmptyStackError):
        s.pop()


def test_with_push():
    s = Stack()
    s.push('a')
    s.push('b')
    s.clear()
    assert bool(s) is False
    assert len(s) == 0
    with pytest.raises(EmptyStackError):
        s.pop()
