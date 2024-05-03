import pytest

from basic_data_structure import LinkedList
from basic_data_structure.exceptions.list_exceptions import (
    ListHasCycleError,
    ListIndexIsNotAnIntError,
    ListIndexOfRangeError,
    ListNegativeIndexError,
)


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


@pytest.mark.parametrize('idx', (0, 1, 2, 10))
def test_empty_list(empty_list: LinkedList, idx: int):
    with pytest.raises(ListIndexOfRangeError):
        _ = empty_list[idx]


@pytest.mark.parametrize('idx', (3, 4, 10))
def test_index_range(str_list: LinkedList, idx: int):
    with pytest.raises(ListIndexOfRangeError):
        _ = str_list[idx]


@pytest.mark.parametrize('idx', (-1, -2, -10))
def test_negative_index(str_list: LinkedList, idx: int):
    with pytest.raises(ListNegativeIndexError):
        _ = str_list[idx]


@pytest.mark.parametrize('idx', range(20))
def test_cycle(cycled_list: LinkedList, idx: int):
    with pytest.raises(ListHasCycleError):
        len(cycled_list)

    item = cycled_list[idx]
    assert item is not None
    assert item.value is not None
    assert item.next is not None


def test_slice(str_list: LinkedList):
    with pytest.raises(ListIndexIsNotAnIntError):
        _ = str_list[:]
