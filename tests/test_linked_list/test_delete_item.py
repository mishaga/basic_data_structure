import pytest

from basic_data_structure import LinkedList
from basic_data_structure.exceptions.list_exceptions import (
    ListIndexIsNotAnIntError,
    ListIndexOfRangeError,
    ListNegativeIndexError,
)


def test_fist(int_list: LinkedList):
    del int_list[0]
    assert list(int_list.values()) == [2, 3]


def test_middle(int_list: LinkedList):
    del int_list[1]
    assert list(int_list.values()) == [1, 3]


def test_last(int_list: LinkedList):
    del int_list[2]
    assert list(int_list.values()) == [1, 2]


def test_not_first(int_list: LinkedList):
    assert list(int_list.values()) == [1, 2, 3]
    del int_list[1]
    assert list(int_list.values()) == [1, 3]
    del int_list[1]
    assert list(int_list.values()) == [1]


@pytest.mark.parametrize('idx', (-1, -2, -3))
def test_negative_index(int_list: LinkedList, idx: int):
    with pytest.raises(ListNegativeIndexError):
        del int_list[idx]


def test_delete_in_loop(int_list: LinkedList):
    assert list(int_list.values()) == [1, 2, 3]
    for _ in range(len(int_list)):
        del int_list[0]
    assert list(int_list) == []


@pytest.mark.parametrize('idx', (0, 1, 2, 10))
def test_empty_list(empty_list: LinkedList, idx: int):
    with pytest.raises(ListIndexOfRangeError) as q:
        del empty_list[idx]
    print(q)


@pytest.mark.parametrize('idx', (3, 4, 10))
def test_index_range(str_list: LinkedList, idx: int):
    with pytest.raises(ListIndexOfRangeError):
        del str_list[idx]


@pytest.mark.parametrize('idx', range(20))
def test_cycle(cycled_list: LinkedList, idx: int):
    del cycled_list[idx]


def test_slice(str_list: LinkedList):
    with pytest.raises(ListIndexIsNotAnIntError):
        del str_list[:]
