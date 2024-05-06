"""# Stack

A stack is a data type that serves as a collection of elements with two main operations –
`push` (adds an element to the collection), and `pop` (removes the most recently added element).

The order is FILO (First In Last Out) which implies that the element that is inserted first,
comes out last.

## Example

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

## Dunder methods

1. `__bool__` – return `False` if the stack is empty, `True` otherwise
   ```python
   while stack:
       value = stack.pop()
   ```
2. `__len__` – return length (count of elements) of the stack
   ```python
   if len(stack) > 2:
       ...
   ```

### A note on iteration

The `__iter__` and `__next__` methods are not implemented **intentionally**. If you want to iterate
over a Stack like this `for i in stack`, you're better off using built-in `list` instead, because
this kind of iteration will implicitly call `pop()` on each iteration. Therefore, your stack
will be empty by the end of a loop.

It is better to call `pop()` **explicitly**, so use `while` loop like this:

```python
while stack:
    element = stack.pop()
    ...
```
"""

from typing import Any

from basic_data_structure.exceptions.stack_exceptions import StackIsEmptyError
from basic_data_structure.nodes.list_node import ListNode


class Stack:
    """Stack data structure.

    LIFO (Last In First Out).
    """

    def __init__(self, *args) -> None:
        """Initialise stack with given sequence of elements.

        `args` could be empty, so the stack will be empty at start

        Time complexity: `O(n)` (when `n` is length of `args`)

        Parameters:
            args: a tuple of values to start with (could be empty)
        """
        self.__length = 0

        previous = None
        pointer = None
        for arg in args:
            pointer = ListNode(value=arg, nxt=previous)
            previous = pointer
            self.__length += 1

        self.__head = pointer

    def __bool__(self) -> bool:
        """Return `False` if the stack is empty, `True` otherwise.

        Time complexity: `O(1)`

        Returns:
            False if the stack is empty, True if there is at least one element
        """
        return self.__length > 0

    def __len__(self) -> int:
        """Return length (count of elements) of the stack.

        Time complexity: `O(1)`

        Returns:
            length of the stack
        """
        return self.__length

    def push(
        self,
        value: Any,  # noqa: WPS110 Found wrong variable name
    ) -> None:
        """Add a new element to the stack.

        Time complexity: `O(1)`

        Parameters:
            value: a value to add to stack
        """
        self.__head = ListNode(value=value, nxt=self.__head)
        self.__length += 1

    def pop(self) -> Any:
        """Retrieve (read and delete) element from the stack.

        Time complexity: `O(1)`

        Returns:
            a value from the head of the stack

        Raises:
            StackIsEmptyError: when stack is empty
        """
        if self.__length == 0:
            raise StackIsEmptyError

        response = self.__head.value
        self.__head = self.__head.next
        self.__length -= 1

        return response

    def clear(self) -> None:
        """Clear the stack.

        Time complexity: `O(1)`
        """
        self.__head = None
        self.__length = 0
