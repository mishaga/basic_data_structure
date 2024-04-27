import pytest

from basic_data_structure import LinkedList, ListNode


def test_empty_list(empty_list: LinkedList):
    assert empty_list.head is None


def test_not_empty(str_list: LinkedList):
    assert str_list.head is not None
    assert str_list.head is str_list[0]


def test_set_none(int_list: LinkedList):
    assert int_list.head is not None
    int_list.head = None
    assert int_list.head is None
    assert bool(int_list) is False
    assert len(int_list) == 0
    assert list(int_list.values()) == []
    assert int_list.has_cycle() is False


def test_set_new(int_list: LinkedList):
    assert int_list.head is not None
    int_list.head = ListNode('new value')
    assert int_list.head is not None
    assert bool(int_list) is True
    assert len(int_list) == 1
    assert list(int_list.values()) == ['new value']
    assert int_list.has_cycle() is False
