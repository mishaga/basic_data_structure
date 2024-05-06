"""# Double linked list value iterator"""

from typing import Any, Optional

from basic_data_structure.nodes.double_linked_list_node import (
    DoubleLinkedListNode,
)


class DoubleLinkedListValueIterator:
    """Double linked list value iterator.

    Iterates through double linked list and returns nodes' values.
    """

    def __init__(
        self,
        pointer: Optional[DoubleLinkedListNode],
        go_forward: bool,
    ) -> None:
        """Init iterator.

        Parameters:
            pointer: double linked list head/tail node
            go_forward: if True, next value would be retrieved with calling "next" property on node,
                        otherwise, "previous" property would be used
        """
        self.__pointer = pointer
        self.__go_forward = go_forward

    def __iter__(self) -> 'DoubleLinkedListValueIterator':
        """Return iterator.

        Returns:
            iterator (self)
        """
        return self

    def __next__(self) -> Any:
        """Retrieve next/previous node's value from double linked list.

        Returns:
            next/previous DoubleLinkedListNode's value

        Raises:
            StopIteration: when reached the end of the double linked list
        """
        if self.__pointer is None:
            raise StopIteration

        response = self.__pointer.value

        if self.__go_forward:
            self.__pointer = self.__pointer.next
        else:
            self.__pointer = self.__pointer.previous

        return response
