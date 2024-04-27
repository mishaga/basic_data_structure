import pytest

from basic_data_structure import LinkedList, ListNode


@pytest.fixture()
def empty_list() -> LinkedList:
    return LinkedList()


@pytest.fixture()
def int_list() -> LinkedList:
    return LinkedList(1, 2, 3)


@pytest.fixture()
def str_list() -> LinkedList:
    return LinkedList('a', 'b', 'c')


@pytest.fixture()
def cycled_list() -> LinkedList:
    last = ListNode(5)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, last))))
    last.next = head
    lst = LinkedList()
    lst.head = head
    return lst
