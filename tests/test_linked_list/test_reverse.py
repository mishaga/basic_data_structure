import pytest

from basic_data_structure import LinkedList
from basic_data_structure.exceptions import ListHasCycleError


def test_empty_list():
    lst = LinkedList()
    assert list(lst.values()) == []
    lst.reverse()
    assert list(lst.values()) == []


def test_one_element():
    lst = LinkedList(1)
    assert list(lst.values()) == [1]
    lst.reverse()
    assert list(lst.values()) == [1]


def test_two_elements():
    lst = LinkedList(1, 2)
    assert list(lst.values()) == [1, 2]
    lst.reverse()
    assert list(lst.values()) == [2, 1]


def test_several_elements():
    lst = LinkedList(1, 2, 3, 4, 5, 6, 7, 8)
    assert list(lst.values()) == [1, 2, 3, 4, 5, 6, 7, 8]
    lst.reverse()
    assert list(lst.values()) == [8, 7, 6, 5, 4, 3, 2, 1]


def test_cycle(cycled_list: LinkedList):
    with pytest.raises(ListHasCycleError):
        cycled_list.reverse()
