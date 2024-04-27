from typing import Any, Optional

from basic_data_structure.exceptions import (
    ListHasCycleError,
    ListIndexError,
    NotListNodeError,
)
from basic_data_structure.list.iterators import (
    ListNodeIterator,
    ListValueIterator,
)
from basic_data_structure.list.list_node import ListNode


class LinkedList:  # noqa: WPS214 Found too many methods
    """Linked list data structure."""

    def __init__(self, *args) -> None:
        """Init a linked list.

        Parameters:
            args: a tuple of values to start with (could be empty)
        """
        self.__head = None

        previous = None
        for arg in args:
            pointer = ListNode(value=arg)
            if self.__head is None:
                self.__head = pointer
            else:
                previous.next = pointer
            previous = pointer

    def __bool__(self) -> bool:
        """Return False if the list is empty, True otherwise.

        Returns:
            False if the list is empty, True if there is at least one element
        """
        return self.__head is not None

    def __len__(self) -> int:
        """Return length of the list.

        Returns:
            length of the list

        Raises:
            ListHasCycleError: when the list has a cycle
        """
        length = 0

        slow = self.__head
        fast = self.__head
        while slow:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
                if fast == slow:
                    raise ListHasCycleError

            length += 1

        return length

    def __getitem__(self, index: int) -> ListNode:
        """Return a node at particular index.

        Parameters:
            index: index

        Returns:
            node at given index
        """
        index = self.__validate_index(index)
        pointer = self.__head
        for _ in range(index):
            pointer = pointer.next
        return pointer

    def __delitem__(self, index: int) -> None:  # noqa: WPS603 Found using restricted magic method
        """Delete a node at particular index.

        Parameters:
            index: index
        """
        index = self.__validate_index(index)

        if index == 0:
            self.__head = self.__head.next
        else:
            previous = None
            pointer = self.__head
            for _ in range(index):
                previous = pointer
                pointer = pointer.next
            previous.next = pointer.next

    def __reversed__(self) -> 'LinkedList':
        """Return a reversed copy of the list.

        Returns:
            a reversed copy of the list

        Raises:
            ListHasCycleError: when the list has a cycle
        """
        new_list = LinkedList()
        slow = self.__head
        fast = self.__head
        while slow:
            new_list.insert(index=0, value=slow.value)
            if fast and fast.next:
                fast = fast.next.next
                if slow == fast:
                    raise ListHasCycleError
            slow = slow.next
        return new_list

    def __iter__(self) -> ListNodeIterator:
        """Return nodes iterator.

        Returns:
            ListNodeIterator
        """
        return ListNodeIterator(self.__head)

    @property
    def head(self) -> Optional[ListNode]:
        """Return head of the list.

        Returns:
            head of the list
        """
        return self.__head

    @head.setter
    def head(self, new_head: Optional[ListNode]) -> None:
        """Set new head.

        Parameters:
            new_head: new ListNode to be a head of the list

        Raises:
            NotListNodeError: when trying to assign not a ListNode or None
        """
        if not isinstance(new_head, (ListNode, type(None))):
            raise NotListNodeError
        self.__head = new_head

    def values(self) -> ListValueIterator:  # noqa: WPS110 Found wrong variable name
        """Return values iterator.

        Returns:
            ListValueIterator
        """
        return ListValueIterator(self.__head)

    def insert(
        self,
        index: int,
        value: Any,  # noqa: WPS110 Found wrong variable name
    ) -> None:
        """Insert a value into given index.

        Parameters:
            index: a position to insert a value to
            value: a value to insert
        """
        length = len(self)

        if index < 0:
            index += length

        if index < 0:
            index = 0

        if index > length:
            index = length

        if index == 0:
            node = ListNode(value, self.__head)
            self.__head = node
        else:
            previous = None
            pointer = self.__head
            for _ in range(index):
                previous = pointer
                pointer = pointer.next
            node = ListNode(value, pointer)
            previous.next = node

    def clear(self) -> None:
        """Clear the list."""
        self.__head = None

    def reverse(self) -> None:
        """Reverse the list.

        Raises:
            ListHasCycleError: when the list has a cycle
        """
        if self.has_cycle():
            raise ListHasCycleError

        pointer = self.__head
        previous = None

        while pointer:
            nxt = pointer.next
            pointer.next = previous
            previous = pointer
            pointer = nxt

        self.__head = previous

    def rotate(self, count: int) -> None:  # noqa: WPS210 Found too many local variables
        """Rotate list.

        To rotate right, pass a positive value.
        To rotate left, pass a negative value.

        Parameters:
            count: number of nodes to shift
        """
        if count == 0:
            return

        length = len(self)
        if length < 2:
            return

        count = count % length  # noqa: WPS350 Found usable augmented assign pattern
        if count == 0:
            return

        pointer = ListNode(None, self.__head)
        new_end = None
        idx = 0
        while pointer.next:
            if idx == length - count:
                new_end = pointer
            pointer = pointer.next
            idx += 1

        new_head = new_end.next
        new_end.next = None
        pointer.next = self.__head
        self.__head = new_head

    def has_cycle(self) -> bool:
        """Return True if the list has cycle.

        Returns:
            True if the list has cycle, False otherwise
        """
        slow = self.__head
        fast = self.__head
        while slow:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
                if fast == slow:
                    return True

        return False

    def __validate_index(self, index: int) -> int:
        """Validate index.

        If given negative index, trying to convert it into positive.

        Parameters:
            index: index to validate

        Returns:
             positive index if it's in rage

         Raises:
             ListIndexError: when given index ins not an integer or when it's out of range
        """
        if not isinstance(index, int):
            raise ListIndexError('Index should be an integer value')

        length = len(self)
        if index < 0:
            index += length

        if index < 0 or length == 0 or index >= length:
            raise ListIndexError('Index out of range')

        return index
