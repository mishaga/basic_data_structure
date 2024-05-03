import pytest

from basic_data_structure import LinkedList, ListNode
from basic_data_structure.exceptions.list_exceptions import ListHasCycleError


def test_empty_list(empty_list: LinkedList):
    assert len(empty_list) == 0


def test_inited_list(str_list: LinkedList):
    assert len(str_list) == 3


def test_with_insert():
    lst = LinkedList()
    lst.insert(0, 'a')
    assert len(lst) == 1


def test_mix(int_list: LinkedList):
    int_list.insert(10, 4)
    int_list.insert(10, 5)
    assert len(int_list) == 5


def test_manual_add(int_list: LinkedList):
    assert len(int_list) == 3

    node = int_list[2]
    assert node.next is None

    node.next = ListNode(4)
    assert len(int_list) == 4


def test_cycle(cycled_list: LinkedList):
    with pytest.raises(ListHasCycleError):
        _ = len(cycled_list)
