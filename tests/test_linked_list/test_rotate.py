import pytest

from basic_data_structure import LinkedList
from basic_data_structure.exceptions.list_exceptions import ListHasCycleError


@pytest.mark.parametrize('count', (1, 2, 3, -1, -10, 100))
def test_empty_list(count: int):
    lst = LinkedList()
    lst.rotate(count)
    assert list(lst.values()) == []


@pytest.mark.parametrize('count', (1, 2, 3, -1, -10, 100))
def test_one_element(count: int):
    lst = LinkedList(1)
    lst.rotate(count)
    assert list(lst.values()) == [1]


@pytest.mark.parametrize('count', (3, -3))
def test_same_length(count):
    lst = LinkedList(1, 2, 3)
    assert list(lst.values()) == [1, 2, 3]
    lst.rotate(count)
    assert list(lst.values()) == [1, 2, 3]


def test_rotate_right():
    lst = LinkedList(1, 2, 3)
    lst.rotate(1)
    assert list(lst.values()) == [3, 1, 2]
    lst.rotate(1)
    assert list(lst.values()) == [2, 3, 1]
    lst.rotate(1)
    assert list(lst.values()) == [1, 2, 3]
    lst.rotate(2)
    assert list(lst.values()) == [2, 3, 1]
    lst.rotate(2)
    assert list(lst.values()) == [3, 1, 2]
    lst.rotate(2)
    assert list(lst.values()) == [1, 2, 3]


def test_rotate_left():
    lst = LinkedList(1, 2, 3)
    lst.rotate(-1)
    assert list(lst.values()) == [2, 3, 1]
    lst.rotate(-1)
    assert list(lst.values()) == [3, 1, 2]
    lst.rotate(-1)
    assert list(lst.values()) == [1, 2, 3]
    lst.rotate(-2)
    assert list(lst.values()) == [3, 1, 2]
    lst.rotate(-2)
    assert list(lst.values()) == [2, 3, 1]
    lst.rotate(-2)
    assert list(lst.values()) == [1, 2, 3]


@pytest.mark.parametrize('count', (-4, -7, -10, -13))
def test_too_small_rotate_left(count: int):
    lst = LinkedList(1, 2, 3)
    lst.rotate(count)
    assert list(lst.values()) == [2, 3, 1]


@pytest.mark.parametrize('count', (4, 7, 10, 13))
def test_too_big_rotate_right(count: int):
    lst = LinkedList(1, 2, 3)
    lst.rotate(count)
    assert list(lst.values()) == [3, 1, 2]


@pytest.mark.parametrize('count', (-1, 1, -2, 2, -3, 3, -100, 100))
def test_cycle(cycled_list: LinkedList, count: int):
    with pytest.raises(ListHasCycleError):
        cycled_list.rotate(count)
