# Basic Data Structure

Implementation of basic sata structures in Python

Supported python versions: `3.9` → `3.12`

Including:
1. [Stack](#stack)
2. [Linked list](#linked-list)
3. [Binary tree](#binary-tree)

Expected data structures in future versions:
1. Queue
2. Double-ended queue
3. Actual binary tree class (now we have `TreeNode` class only)
4. Red-black tree

# Stack

A stack is a data type that serves as a collection of elements with two main operations –
`push` (adds an element to the collection), and `pop` (removes the most recently added element).

## Methods

### `def __init__(*args) -> None`
Initialises stack with given sequence of elements  
This sequence (`args`) could be empty, so the stack will be empty at start

Example:
```python
initially_empty_stack = Stack()
not_empty_stack = Stack(1, 2, 3)  # the order of elements is stack will be reversed
```

### `def __bool__() -> bool`
Returns `False` if stack is empty  
If stack contains at least one element, returns `True`

### `def __len__() -> int`
Returns length (count of elements) of the stack  
If the stack is empty, returns `0`

### `def push(value: Any) -> None`
Adds element to the stack

### `def pop() -> Any`
Pops the last element from the stack  
Function returns the element and deletes it from the stack
If the stack is empty, this function raises `EmptyStackError` exception

### `def clear() -> None`
Clears the stack (removes all the elements)  
Length of the stack afterward will be equal to `0`

## Example

```python
from basic_data_structure import Stack


def init_from_iterable() -> None:
    print('Init from iterable:')

    stack = Stack(0, 1, 2, 3, 4, 5)
    # or like this:
    # stack = Stack(*[0, 1, 2, 3, 4, 5])
    # stack = Stack(*range(6))
    stack.push(6)
    stack.push(7)
    stack.push(8)
    print('Stack length:', len(stack))

    while stack:
        value = stack.pop()
        print(value, end=' ')

    print('')


def manual_pushing() -> None:
    print('Manual pushing:')

    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')

    while stack:
        value = stack.pop()
        print(value, end=' ')

    print('')


if __name__ == '__main__':
    init_from_iterable()
    manual_pushing()
```

The `__iter__` and `__next__` methods are not implemented intentionally.  
If you want to iterate over a Stack like this `for i in stack`, you're better off
using built-in list instead, because this kind of iteration will implicitly
call `pop()` on each iteration. Therefore, your stack will be empty by the end
of a loop.  
It is better to call `pop()` explicitly, so use while loop like this:

```python
while stack:
    element = stack.pop()
    ...
```


# Linked list

A linked list is a linear collection of data elements whose order is not given by their physical
placement in memory. Instead, each element points to the next. It is a data structure consisting
of a collection of nodes which together represent a sequence.

## Methods

### `def __init__(*args) -> None`
Initialises list with given sequence of elements  
This sequence (`args`) could be empty, so the list will be empty at the start

Example:
```python
initially_empty_list = LinkedList()
not_empty_list = LinkedList(1, 2, 3)
```

### `def __bool__() -> bool`
Returns `False` if the list is empty  
If list contains at least one element, returns `True`

### `def __len__() -> int`
Returns length (count of elements) in the list  
If the list is empty, returns `0`  

If the list contains a cycle, raises `ListHasCycleError` exception  
This is `O(n)` operation

### `def __getitem__(index: int) -> ListNode`
Returns a node at particular index

If index is out of range, raises `ListIndexError` exception  
If the list contains a cycle, raises `ListHasCycleError` exception  
Negative indexes supported  
Slices are not supported  
This is `O(n)` operation

Example:
```python
lst = LinkedList(1, 2, 3)
node = lst[1]  # will return node with value `2`
# to retrieve value itself, use attr `value`
print(node.value)  # will print out `2`
```

### `def __delitem__(index: int) -> None`
Returns a node at particular index

If index is out of range, raises `ListIndexError` exception  
If the list contains a cycle, raises `ListHasCycleError` exception  
Negative indexes supported  
Slices are not supported  
This is `O(n)` operation

Example:
```python
lst = LinkedList(1, 2, 3)
del lst[1]  # will delete node with value `2`
```

### `def __reversed__() -> LinkedList`
Returns a reversed copy of the list, the original list remains the same

If the list contains a cycle, raises `ListHasCycleError` exception  
This is `O(n)` operation

Example:
```python
lst = LinkedList(1, 2, 3)
rev = reversed(lst)  # contains nodes `3` → `2` → `1`
```

### `def __iter__() -> ListNodeIterator`
Returns an iterator, each call `next` method on which returns a `ListNode`

Example:
```python
lst = LinkedList(1, 2, 3)
for node in list:
    print(node.value)
```

### `def values() -> ListValueIterator`
Returns an iterator, each call `next` method on which returns a value of a node

Example:
```python
lst = LinkedList(1, 2, 3)
for val in list.values():
    print(val)
```

### `def insert(index: int, value: Any) -> None`
Insert a value into given index  
Mind, that "value" in this case is not a `ListNode`, but actual value of a future node

If the index is greater than or equal to the length of the list, the element will be inserted
at the end of the list. If the negative index is out of range, the element will be inserted
at the beginning of the list.

If the list contains a cycle, raises `ListHasCycleError` exception  
Negative indexes supported  
This is `O(n)` operation

Example:
```python
lst = LinkedList(1, 3)
lst.insert(1, 2)  # will add element betwin `1` and `3`
lst.insert(len(lst), 4)  # will add to the end
lst.insert(100, 5)  # will add to the end
lst.insert(-6, 0)  # will add to the beginning
lst.insert(-100, -1)  # will add to the beginning
```

### `def clear() -> None`
Clears the list (removes all the elements)  
The length of the list afterward will be equal to `0`

### `def reverse() -> None`
Reverses the list  
Unlike `reversed(lst)`, `lst.reverse()` will rearrange the list itself and will return `None`

If the list contains a cycle, raises `ListHasCycleError` exception  
This is `O(n)` operation

Example:
```python
lst = LinkedList(1, 2, 3)  # contains nodes `1` → `2` → `3`
lst.reverse()  # now contains nodes `3` → `2` → `1`
```

### `def rotate(count: int) -> None`
Rotates (shifts) list to the right or left

If the list contains a cycle, raises `ListHasCycleError` exception  
This is `O(n)` operation

Example:
```python
lst = LinkedList(1, 2, 3, 4, 5)  # `1` → `2` → `3` → `4` → `5`
lst.rotate(1)                    # `5` → `1` → `2` → `3` → `4`
lst.rotate(-2)                   # `2` → `3` → `4` → `5` → `1` 
```

### `def has_cycle() -> bool`
Returns `True` if the list contains cycle, `False` otherwise

This is `O(n)` operation

Example:
```python
lst = LinkedList(1, 2, 3, 4, 5)
print(lst.has_cycle())  # False
lst[-1].next = lst[0]
print(lst.has_cycle())  # True
```

### property `def head() -> Optional[ListNode]`
If you want to iterate through the sequence of nodes by yourself, feel free
to use `head` property of the list.  
If the list is empty, property will return `None`

### property setter `def head(new_head: Optional[ListNode]) -> None`
Sets new head to the list  
Clears the list, if new head is `None`

## Examples

```python
from basic_data_structure import LinkedList


def main():
    lst = LinkedList(8, 7, 6, 5, 3)

    lst.insert(4, 4)
    lst.insert(100, 2)
    lst.insert(0, 9)
    lst.insert(0, 1)

    lst.rotate(-1)
    lst.reverse()

    for val in lst.values():
        print(val, end=' ')


if __name__ == '__main__':
    main()
```

If you'd like to create linked list by yourself, you can use `ListNode` class like this, for example:

```python
from basic_data_structure import ListNode


def main():
    head = ListNode(1, ListNode(2, ListNode(3)))
    while head:
        print(head.value, end=' ')
        head = head.next


if __name__ == '__main__':
    main()
```


## Binary tree

A binary tree is a tree data structure in which each node has at most two children,
referred to as the left child and the right child.

There is no `BinaryTree` class so far in the project, but you can create a tree
using `TreeNode` class like this:

```python
from typing import Generator, Optional

from basic_data_structure import TreeNode


def generate_tree() -> TreeNode:
    """Generate binary tree.

                 8
          ┌──────┴───────┐
          4              12
      ┌───┴───┐       ┌───┴───┐
      2       6       10      14
    ┌─┴─┐   ┌─┴─┐   ┌─┴─┐   ┌─┴─┐
    1   3   5   7   9   11  13  15
    """
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
    """Depth-first search."""
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


if __name__ == '__main__':
    main()
```
