"""# List node iterator"""

from typing import Optional

from basic_data_structure.nodes.list_node import ListNode


class ListNodeIterator:
    """Linked list node iterator.

    Iterates through list and returns ListNode.
    """

    def __init__(self, head: Optional[ListNode]) -> None:
        """Init iterator.

        Parameters:
            head: linked list head node
        """
        self.__pointer = head

    def __iter__(self) -> 'ListNodeIterator':
        """Return iterator.

        Returns:
            iterator (self)
        """
        return self

    def __next__(self) -> ListNode:
        """Retrieve next node from linked list.

        Returns:
            next ListNode

        Raises:
            StopIteration: when reached the end of the list
        """
        if self.__pointer is None:
            raise StopIteration

        response = self.__pointer
        self.__pointer = self.__pointer.next
        return response
