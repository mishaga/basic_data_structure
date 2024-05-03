"""# List value iterator"""

from typing import Any, Optional

from basic_data_structure.nodes.list_node import ListNode


class ListValueIterator:
    """Linked list value iterator.

    Iterates through list and returns value of a ListNode.
    """

    def __init__(self, head: Optional[ListNode]) -> None:
        """Init iterator.

        Parameters:
            head: linked list head node
        """
        self.__pointer = head

    def __iter__(self) -> 'ListValueIterator':
        """Return iterator.

        Returns:
            iterator (self)
        """
        return self

    def __next__(self) -> Any:
        """Retrieve next value from linked list.

        Returns:
            value of next ListNode

        Raises:
            StopIteration: when reached the end of the list
        """
        if self.__pointer is None:
            raise StopIteration

        response = self.__pointer.value
        self.__pointer = self.__pointer.next
        return response
