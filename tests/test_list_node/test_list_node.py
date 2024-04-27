from typing import Any

import pytest

from basic_data_structure import ListNode


@pytest.mark.parametrize('value', (0, 1, 'a', None, object, object()))
def test_value(value: Any):
    head = ListNode(value)
    assert head.value is value


def test_no_next_item():
    head = ListNode(1)
    assert head.next is None


def test_next_item_explicit():
    head = ListNode(1)
    head.next = ListNode(2)
    assert head.next is not None


def test_next_item_on_create():
    head = ListNode(1, ListNode(2))
    assert head.next is not None


def test_while_loop():
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

    i = 0
    while head:
        assert head.value == i
        head = head.next
        i += 1

    assert head is None
    assert i == 5
