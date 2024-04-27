import pytest

from basic_data_structure import Stack


def test_empty_stack():
    s = Stack()
    assert len(s) == 0


@pytest.mark.parametrize('sequence', (
    [1],
    ['a', 'b', 'c'],
    [object()],
))
def test_inited_stack(sequence: list):
    s = Stack(*sequence)
    assert len(s) == len(sequence)


def test_pushed_stack():
    s = Stack()
    s.push(0)
    s.push(1)
    assert len(s) == 2


def test_mix():
    s = Stack(1, 2, 3)
    s.push(4)
    s.push(5)
    assert len(s) == 5
