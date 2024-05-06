"""# Double linked list node iterator"""

from typing import Optional

from basic_data_structure.nodes.double_linked_list_node import (
    DoubleLinkedListNode,
)


class DoubleLinkedListNodeIterator:
    """Double linked list node iterator.

    Iterates through double linked list and returns DoubleLinkedListNode.
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

    def __iter__(self) -> 'DoubleLinkedListNodeIterator':
        """Return iterator.

        Returns:
            iterator (self)
        """
        return self

    def __next__(self) -> DoubleLinkedListNode:
        """Retrieve next/previous node from double linked list.

        Returns:
            next/previous DoubleLinkedListNode

        Raises:
            StopIteration: when reached the end of the double linked list
        """
        if self.__pointer is None:
            raise StopIteration

        response = self.__pointer

        if self.__go_forward:
            self.__pointer = self.__pointer.next
        else:
            self.__pointer = self.__pointer.previous

        return response
