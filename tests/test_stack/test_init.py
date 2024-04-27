import pytest

from basic_data_structure import Stack


def test_init_with_args():
    s = Stack(1, 2, 3)
    assert len(s) == 3


@pytest.mark.parametrize('size', (0, 1, 3, 5, 1000))
def test_init_asterisk(size: int):
    s = Stack(*range(size))
    assert len(s) == size
