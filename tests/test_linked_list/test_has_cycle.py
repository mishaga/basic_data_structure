import pytest

from basic_data_structure import LinkedList, ListNode


def test_cycle(cycled_list: LinkedList):
    assert cycled_list.has_cycle() is True


@pytest.mark.parametrize('idx', (0, 1, 2))
def test_different_indexes(str_list: LinkedList, idx: int):
    assert str_list.has_cycle() is False
    last = str_list[2]
    last.next = str_list[idx]
    assert str_list.has_cycle() is True


def test_one_element():
    lst = LinkedList()
    assert lst.has_cycle() is False
    node = ListNode(1)
    node.next = node
    lst.head = node
    assert lst.has_cycle() is True
    node.next = None
    assert lst.has_cycle() is False
