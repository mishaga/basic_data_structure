"""# Basic data structures in python

Implementation of basic sata structures in Python

Including:
1. [Stack](basic_data_structure/stack.html)
2. [Linked list](basic_data_structure/linked_list.html)
3. [Binary tree](basic_data_structure/nodes/tree_node.html)

Expected data structures in future versions:
1. Queue
2. Double-ended queue
3. Actual binary tree class (now package contains `TreeNode` class only)
4. Red-black tree

Supported python versions: `3.9` → `3.12`

Links:

* [GitHub](https://github.com/mishaga/basic_data_structure)
* [PyPi](https://pypi.org/project/basic-data-structure/)
* [Documentation](https://mishaga.github.io/basic_data_structure/)

Installation:

```bash
pip install basic-data-structure
```

## Examples

### Stack

```python
from basic_data_structure import Stack


def main() -> None:
    # to initialise empty stack do this: stack = Stack()

    stack = Stack(0, 1, 2, 3, 4, 5)
    # or like this: stack = Stack(*[0, 1, 2, 3, 4, 5])
    # or like this: stack = Stack(*range(6))

    stack.push(6)
    stack.push(7)
    stack.push(8)

    print('Stack length:', len(stack))

    while stack:
        value = stack.pop()
        print(value, end=' ')

    # Output: 8 7 6 5 4 3 2 1 0


if __name__ == '__main__':
    main()

```

### Linked list

```python
from basic_data_structure import LinkedList


def main():
    lst = LinkedList('oops', 8, 7, 6, 5, 3)

    del lst[0]  # delete node
    node = lst[4]  # get node

    print('Saved node:', node.value)

    lst.insert(4, 4)  # insert new value into list
    lst.append(2)  # append a new value
    lst.prepend(9)  # prepend a new value (ad to the beginning)
    lst.prepend(1)

    lst.rotate(-1)  # rotate (shift) the list
    lst.reverse()  # reverse list

    print('List length:', len(lst))  # length of the list

    for val in lst.values():
        # iteration over values
        print(val, end=' ')

    # Output: 1 2 3 4 5 6 7 8 9

    print('')

    for node in lst:
        # iteration over nodes
        print(node.value, end=' ')

    # Output: 1 2 3 4 5 6 7 8 9


if __name__ == '__main__':
    main()

```

### Binary tree

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


from basic_data_structure.double_linked_list import DoubleLinkedList
from basic_data_structure.linked_list import LinkedList
from basic_data_structure.nodes.double_linked_list_node import (
    DoubleLinkedListNode,
)
from basic_data_structure.nodes.list_node import ListNode
from basic_data_structure.nodes.tree_node import TreeNode
from basic_data_structure.queue import Queue
from basic_data_structure.stack import Stack
