from typing import Any

from basic_data_structure.exceptions import EmptyStackError
from basic_data_structure.list.list_node import ListNode


class Stack:
    """Stack data structure.

    LIFO (Last In, First Out).
    """

    def __init__(self, *args) -> None:
        """Init a stack.

        Parameters:
            args: a tuple of values to start with (could be empty)
        """
        length = 0
        previous = None
        pointer = None
        for arg in args:
            pointer = ListNode(value=arg, nxt=previous)
            previous = pointer
            length += 1

        self.__head = pointer
        self.__length = length

    def __bool__(self) -> bool:
        """Return False if the stack is empty, True otherwise.

        Returns:
            False if the stack is empty, True if there is at least one element
        """
        return self.__length > 0

    def __len__(self) -> int:
        """Return length of the stack.

        Returns:
            length of the stack
        """
        return self.__length

    def push(
        self,
        value: Any,  # noqa: WPS110 Found wrong variable name
    ) -> None:
        """Add a new element to the stack.

        Parameters:
            value: a value to add to stack
        """
        self.__head = ListNode(value=value, nxt=self.__head)
        self.__length += 1

    def pop(self) -> Any:
        """Retrieve element from the stack.

        Returns:
            a value from the head of the stack

        Raises:
            EmptyStackError: when stack is empty
        """
        if self.__length == 0:
            raise EmptyStackError

        response = self.__head.value
        self.__head = self.__head.next
        self.__length -= 1

        return response

    def clear(self) -> None:
        """Clear the stack."""
        self.__head = None
        self.__length = 0
