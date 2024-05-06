"""# Queue"""

from typing import Any

from basic_data_structure.exceptions.queue_exceptions import QueueIsEmptyError
from basic_data_structure.nodes.list_node import ListNode


class Queue:
    """Queue data structure.

    FIFO (First In First Out).
    """

    def __init__(self, *args) -> None:
        """Initialise queue with given sequence of elements.

        `args` could be empty, so the queue will be empty at start

        Time complexity: `O(n)` (when `n` is length of `args`)

        Parameters:
            args: a tuple of values to start with (could be empty)
        """
        self.__head = None
        self.__tail = None
        self.__length = 0

        previous = None
        pointer = None
        for arg in args:
            pointer = ListNode(value=arg)

            if previous:
                previous.next = pointer

            if self.__head is None:
                self.__head = pointer

            previous = pointer
            self.__length += 1

        self.__tail = pointer

    def __bool__(self) -> bool:
        """Return `False` if the queue is empty, `True` otherwise.

        Time complexity: `O(1)`

        Returns:
            False if the queue is empty, True if there is at least one element
        """
        return self.__length > 0

    def __len__(self) -> int:
        """Return length (count of elements) of the queue.

        Time complexity: `O(1)`

        Returns:
            length of the queue
        """
        return self.__length

    # def add(
    #     self,
    #     value: Any,  # noqa: WPS110 Found wrong variable name
    # ) -> None:
    #     """Add a new element to the stack.
    #
    #     Time complexity: `O(1)`
    #
    #     Parameters:
    #         value: a value to add to stack
    #     """
    #     self.__tail = ListNode(value=value, nxt=self.__tail)
    #     self.__length += 1
    #
    # def pop(self) -> Any:
    #     """Retrieve (read and delete) element from the stack.
    #
    #     Time complexity: `O(1)`
    #
    #     Returns:
    #         a value from the head of the stack
    #
    #     Raises:
    #         StackIsEmptyError: when stack is empty
    #     """
    #     if self.__length == 0:
    #         raise QueueIsEmptyError
    #
    #     response = self.__head.value
    #     self.__head = self.__head.next
    #     self.__length -= 1
    #
    #     return response

    @property
    def h(self) -> Any:
        return self.__head.value if self.__head else None

    @property
    def t(self) -> Any:
        return self.__tail.value if self.__tail else None

    def clear(self) -> None:
        """Clear the queue.

        Time complexity: `O(1)`
        """
        self.__head = None
        self.__tail = None
        self.__length = 0
