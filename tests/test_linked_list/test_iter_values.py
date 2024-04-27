import pytest

from basic_data_structure import LinkedList, ListNode
from basic_data_structure.list.iterators import ListValueIterator


def test_iterator():
    lst = LinkedList()
    iterator = lst.values()
    assert isinstance(iterator, ListValueIterator)


def test_empty_list():
    lst = LinkedList()
    iterator = lst.values()
    with pytest.raises(StopIteration):
        next(iterator)


def test_next():
    lst = LinkedList(1)
    iterator = lst.values()
    item = next(iterator)
    assert isinstance(item, int)
    assert item == 1

    with pytest.raises(StopIteration):
        next(iterator)


def test_loop():
    lst = LinkedList(1, 2, 3, 4, 5)
    idx = 0
    for item in lst.values():
        assert item == idx + 1
        assert item == lst[idx].value
        idx += 1


def test_cycle(cycled_list: LinkedList):
    expected = [1, 2, 3, 4, 5] * 3
    actual = []

    iterator = cycled_list.values()
    for _ in range(15):
        actual.append(next(iterator))

    assert expected == actual
