import pytest

from basic_data_structure import LinkedList
from basic_data_structure.exceptions.list_exceptions import ListHasCycleError


def test_empty_list(empty_list: LinkedList):
    empty_list.append('a')
    assert list(empty_list.values()) == ['a']


def test_not_empty(str_list: LinkedList):
    str_list.append('d')
    assert list(str_list.values()) == ['a', 'b', 'c', 'd']


def test_cycle(cycled_list: LinkedList):
    with pytest.raises(ListHasCycleError):
        cycled_list.append(6)
