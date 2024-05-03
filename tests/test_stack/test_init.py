import pytest

from basic_data_structure import Stack


def test_init_with_args():
    stack = Stack(1, 2, 3)
    assert len(stack) == 3


@pytest.mark.parametrize('size', (0, 1, 3, 5, 1000))
def test_init_asterisk(size: int):
    stack = Stack(*range(size))
    assert len(stack) == size
