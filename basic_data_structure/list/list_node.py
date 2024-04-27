from typing import Any, Optional


class ListNode:
    """A node of a linked list."""

    def __init__(
        self,
        value: Any,  # noqa: WPS110 Found wrong variable name
        nxt: Optional['ListNode'] = None,
    ):
        """Init a list node.

        Parameters:
            value: a value of the node
            nxt: (optional) next node
        """
        self.value = value  # noqa: WPS110 Found wrong variable name
        self.next = nxt
