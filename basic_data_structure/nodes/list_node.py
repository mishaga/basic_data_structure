"""# List node

An element of a `LinkedList` data structure.

Contains a value and a link to the next node.
If this node is the last one, link to the next node will be `None`.

# Example

```python
from basic_data_structure import ListNode


def main():
    head = ListNode(1, ListNode(2, ListNode(3)))
    while head:
        print(head.value, end=' ')
        head = head.next

    # Output: 1 2 3


if __name__ == '__main__':
    main()

```
"""

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
            nxt: (optional) link to next node
        """
        self.value = value  # noqa: WPS110 Found wrong variable name
        self.next = nxt
