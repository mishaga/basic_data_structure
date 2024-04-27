import pytest

from basic_data_structure import LinkedList, ListNode
from basic_data_structure.exceptions import ListHasCycleError
from basic_data_structure.list.iterators import ListNodeIterator


def test_iterator(empty_list: LinkedList):
    iterator = iter(empty_list)
    assert isinstance(iterator, ListNodeIterator)


def test_empty_list(empty_list: LinkedList):
    iterator = iter(empty_list)
    with pytest.raises(StopIteration):
        next(iterator)


def test_next():
    lst = LinkedList(1)
    iterator = iter(lst)
    item = next(iterator)
    assert isinstance(item, ListNode)
    assert item.value == 1
    assert item.next is None

    with pytest.raises(StopIteration):
        next(iterator)


def test_loop():
    lst = LinkedList(1, 2, 3, 4, 5)
    idx = 0
    for item in lst:
        if idx < 4:
            assert item.next is not None
        else:
            assert item.next is None
        assert item.value == idx + 1
        assert item is lst[idx]
        idx += 1


def test_cycle(cycled_list: LinkedList):
    expected = [1, 2, 3, 4, 5] * 3
    actual = []

    iterator = iter(cycled_list)
    for _ in range(15):
        actual.append(next(iterator).value)

    assert expected == actual
