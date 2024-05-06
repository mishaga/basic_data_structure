"""# Double linked list node"""

from typing import Any, Optional


class DoubleLinkedListNode:
    """A node of a double linked list."""

    def __init__(
        self,
        value: Any,  # noqa: WPS110 Found wrong variable name
        previous: Optional['DoubleLinkedListNode'] = None,
        nxt: Optional['DoubleLinkedListNode'] = None,
    ):
        """Init a list node.

        Parameters:
            value: a value of the node
            previous: (optional) link to previous node
            nxt: (optional) link to next node
        """
        self.value = value  # noqa: WPS110 Found wrong variable name
        self.previous = previous
        self.next = nxt
