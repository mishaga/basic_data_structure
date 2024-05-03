"""# Tree node

An element (node) of a binary tree

A binary tree is a data structure in which each node has at most two children,
referred to as the left child and the right child.

`TreeNode` contains a value and links to the left and right nodes.
This links could be empty (i.e. `None`). If there is no links to both left
and right nodes, the node is considered to be a "leaf".

There is no `BinaryTree` class so far in the project, but you can create a tree
using `TreeNode` like show in example

# Example

```python
from typing import Generator, Optional

from basic_data_structure import TreeNode


def generate_tree() -> TreeNode:
    \"""Generate binary tree.

                 8
          ┌──────┴───────┐
          4              12
      ┌───┴───┐       ┌───┴───┐
      2       6       10      14
    ┌─┴─┐   ┌─┴─┐   ┌─┴─┐   ┌─┴─┐
    1   3   5   7   9   11  13  15
    \"""
    return TreeNode(
        8,
        left=TreeNode(
            4,
            left=TreeNode(
                2,
                left=TreeNode(1),
                right=TreeNode(3),
            ),
            right=TreeNode(
                6,
                left=TreeNode(5),
                right=TreeNode(7),
            ),
        ),
        right=TreeNode(
            12,
            left=TreeNode(
                10,
                left=TreeNode(9),
                right=TreeNode(11),
            ),
            right=TreeNode(
                14,
                left=TreeNode(13),
                right=TreeNode(15),
            ),
        ),
    )


def dfs(root: Optional[TreeNode]) -> Generator[int, None, None]:
    \"""Depth-first search.\"""
    if root:
        if root.left:
            yield from dfs(root.left)

        yield root.value

        if root.right:
            yield from dfs(root.right)


def main():
    print('Depth-first search (DFS)')
    for data in dfs(root=generate_tree()):
        print(data, end=' ')

    # Output:
    # Depth-first search (DFS)
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15


if __name__ == '__main__':
    main()

```
"""

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
