import pytest

from basic_data_structure import LinkedList
from basic_data_structure.exceptions import ListIndexError, ListHasCycleError


def test_fist():
    lst = LinkedList()
    lst.insert(0, 1)
    lst.insert(1, 2)
    lst.insert(2, 3)
    assert list(lst.values()) == [1, 2, 3]
    del lst[0]
    assert list(lst.values()) == [2, 3]


def test_not_first(int_list: LinkedList):
    assert list(int_list.values()) == [1, 2, 3]
    del int_list[1]
    assert list(int_list.values()) == [1, 3]
    del int_list[1]
    assert list(int_list.values()) == [1]


def test_negative_index(int_list: LinkedList):
    del int_list[-2]
    assert list(int_list.values()) == [1, 3]
    del int_list[-1]
    assert list(int_list.values()) == [1]
    del int_list[-1]
    assert list(int_list.values()) == []


def test_delete_in_loop(int_list: LinkedList):
    assert list(int_list.values()) == [1, 2, 3]
    for _ in range(len(int_list)):
        del int_list[0]
    assert list(int_list) == []


@pytest.mark.parametrize('idx', (0, 1, -1, 2, -2, 10, -10))
def test_empty_list(empty_list: LinkedList, idx: int):
    with pytest.raises(ListIndexError):
        del empty_list[idx]


@pytest.mark.parametrize('idx', (3, -4, 10, -10))
def test_index_range(str_list: LinkedList, idx: int):
    with pytest.raises(ListIndexError):
        del str_list[idx]


def test_cycle(cycled_list: LinkedList):
    with pytest.raises(ListHasCycleError):
        del cycled_list[0]
