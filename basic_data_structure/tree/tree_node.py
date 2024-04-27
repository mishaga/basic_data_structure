from typing import Any, Optional


class TreeNode:
    """A node of a binary tree."""

    def __init__(
        self,
        value: Any,  # noqa: WPS110 Found wrong variable name
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None,
    ) -> None:
        """Init a tree node.

        Parameters:
            value: a value of the node
            left: (optional) left child of the node
            right: (optional) right child of the node
        """
        self.value = value  # noqa: WPS110 Found wrong variable name
        self.left = left
        self.right = right
