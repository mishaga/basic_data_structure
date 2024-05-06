"""# Double linked list"""

from typing import Any, Optional

from basic_data_structure.exceptions.list_exceptions import (
    ListHasCycleError,
    ListIndexIsNotAnIntError,
    ListIndexOfRangeError,
)
from basic_data_structure.iterators.double_linked_list_node_iterator import (
    DoubleLinkedListNodeIterator,
)
from basic_data_structure.iterators.double_linked_list_value_iterator import (
    DoubleLinkedListValueIterator,
)
from basic_data_structure.nodes.double_linked_list_node import (
    DoubleLinkedListNode,
)


class DoubleLinkedList:
    """Double linked list data structure."""

    def __init__(self, *args) -> None:
        """Initialise a double linked list with given sequence of elements.

        `args` could be empty, so the list will be empty at the start

        Time complexity: `O(n)` (when `n` is length of `args`)

        Parameters:
            args: a tuple of values to start with (could be empty)
        """
        self.__head = None
        self.__tail = None

        previous = None
        for arg in args:
            node = DoubleLinkedListNode(value=arg, previous=previous)
            if self.__head is None:
                self.__head = node
            else:
                previous.next = node
            previous = node

        self.__tail = previous

    def __bool__(self) -> bool:
        """Return `False` if the list is empty, `True` otherwise.

        Time complexity: `O(1)`

        Returns:
            `False` if the list is empty, `True` if there is at least one element
        """
        return self.__head is not None

    def __len__(self) -> int:
        """Return length (count of elements) of the list.

        Time complexity: `O(n)`

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

    def __getitem__(self, index: int) -> DoubleLinkedListNode:
        """Return a node at particular index.

        Mind that actual `DoubleLinkedListNode` will be returned, not its value

        Time complexity: `O(n)`

        Parameters:
            index: index (zero, positive or negative)

        Returns:
            node at given index

        Raises:
            ListIndexOfRangeError: when there is no such index in the list
        """
        if not isinstance(index, int):
            raise ListIndexIsNotAnIntError

        if self.__head is None:
            raise ListIndexOfRangeError

        # todo ...
        if index < 0:
            ...
        else:
            ...

        # pointer = self.__head
        # idx = 0
        # while pointer:
        #     if idx == index:
        #         return pointer
        #     pointer = pointer.next
        #     idx += 1
        #
        # raise ListIndexOfRangeError

    @property
    def head(self) -> Optional[DoubleLinkedListNode]:
        """..."""
        return self.__head

    @property
    def tail(self) -> Optional[DoubleLinkedListNode]:
        """..."""
        return self.__tail

    def go_forward(self):
        """..."""
        return DoubleLinkedListNodeIterator(pointer=self.__head, go_forward=True)

    def go_backwards(self):
        """..."""
        return DoubleLinkedListNodeIterator(pointer=self.__tail, go_forward=False)
