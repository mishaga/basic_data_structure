import pytest

from basic_data_structure import LinkedList
from basic_data_structure.exceptions import ListIndexError, ListHasCycleError


def test_get_item(int_list: LinkedList):
    int_list.insert(len(int_list), 4)

    assert int_list[3].value == 4
    assert int_list[2].value == 3
    assert int_list[1].value == 2
    assert int_list[0].value == 1


def test_negative_index(int_list: LinkedList):
    int_list.insert(len(int_list), 4)

    assert int_list[-1].value == 4
    assert int_list[-2].value == 3
    assert int_list[-3].value == 2
    assert int_list[-4].value == 1


@pytest.mark.parametrize('idx', (0, 1, -1, 2, -2, 10, -10))
def test_empty_list(empty_list: LinkedList, idx: int):
    with pytest.raises(ListIndexError):
        _ = empty_list[idx]


@pytest.mark.parametrize('idx', (3, -4, 10, -10))
def test_index_range(str_list: LinkedList, idx: int):
    with pytest.raises(ListIndexError):
        _ = str_list[idx]


@pytest.mark.parametrize('idx', (-2, -1, 0, 1, 2, 10))
def test_cycle(cycled_list: LinkedList, idx: int):
    with pytest.raises(ListHasCycleError):
        _ = cycled_list[idx]
