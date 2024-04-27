import pytest

from basic_data_structure import LinkedList
from basic_data_structure.exceptions import ListHasCycleError


def test_empty_list():
    lst = LinkedList()
    lst.insert(0, 'a')
    assert list(lst.values()) == ['a']


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


def test_negative_one_index():
    lst = LinkedList('a', 'b', 'd')
    lst.insert(-1, 'c')
    assert list(lst.values()) == ['a', 'b', 'c', 'd']


def test_negative_two_index():
    lst = LinkedList('a', 'c', 'd')
    lst.insert(-2, 'b')
    assert list(lst.values()) == ['a', 'b', 'c', 'd']


def test_negative_equals_zero():
    lst = LinkedList('b', 'c', 'd')
    lst.insert(-3, 'a')
    assert list(lst.values()) == ['a', 'b', 'c', 'd']


@pytest.mark.parametrize('idx', (-4, -5, -10, -100))
def test_too_low_index(int_list: LinkedList, idx: int):
    int_list.insert(idx, 0)
    assert list(int_list.values()) == [0, 1, 2, 3]


@pytest.mark.parametrize('idx', (4, 5, 10, 100))
def test_too_high_index(int_list: LinkedList, idx: int):
    int_list.insert(idx, 4)
    assert list(int_list.values()) == [1, 2, 3, 4]


def test_cycle(cycled_list: LinkedList):
    with pytest.raises(ListHasCycleError):
        cycled_list.insert(0, 0)
