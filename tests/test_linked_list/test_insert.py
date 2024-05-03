import pytest

from basic_data_structure import LinkedList
from basic_data_structure.exceptions.list_exceptions import ListNegativeIndexError


@pytest.mark.parametrize('idx', (0, 1, 2, 10))
def test_empty_list(empty_list: LinkedList, idx: int):
    empty_list.insert(idx, 'a')
    assert list(empty_list.values()) == ['a']


def test_insert_between():
    lst = LinkedList('a', 'c')
    lst.insert(1, 'b')
    assert list(lst.values()) == ['a', 'b', 'c']


def test_insert_between_many():
    lst = LinkedList(0, 1, 2, 3, 4, 5, 7)
    lst.insert(6, 6)
    assert list(lst.values()) == list(range(8))


def test_prepend():
    lst = LinkedList('b', 'c')
    lst.insert(0, 'a')
    assert list(lst.values()) == ['a', 'b', 'c']


def test_append():
    lst = LinkedList('a', 'b', 'c')
    lst.insert(len(lst), 'd')
    assert list(lst.values()) == ['a', 'b', 'c', 'd']


@pytest.mark.parametrize('idx', (-1, -2, -3, -10, -100))
def test_negative_index(int_list: LinkedList, idx: int):
    with pytest.raises(ListNegativeIndexError):
        int_list.insert(idx, 'any value')


@pytest.mark.parametrize('idx', (4, 5, 10, 100))
def test_too_high_index(int_list: LinkedList, idx: int):
    int_list.insert(idx, 4)
    assert list(int_list.values()) == [1, 2, 3, 4]


@pytest.mark.parametrize('idx', range(10))
def test_cycle(cycled_list: LinkedList, idx: int):
    cycled_list.insert(idx, 'new value')
