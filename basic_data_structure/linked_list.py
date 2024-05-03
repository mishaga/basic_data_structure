"""# Linked list

A linked list is a linear collection of data elements whose order is not given by their physical
placement in memory. Instead, each element points to the next. It is a data structure consisting
of a collection of nodes which together represent a sequence.

## Example

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

## Dunder methods

1. `__bool__` – return `False` if the list is empty, `True` otherwise
   ```python
   if linked_list:
       ...
   ```
2. `__len__` – return length (count of elements) of the list
   ```python
   if len(linked_list) > 2:
       ...
   ```
3. `__getitem__` – return a node at particular index
   ```python
   second_node = linked_list[2]
   # mind that actual "ListNode" will be returned, not its value
   # mind that negative indexes or slices are not supported
   ```
4. `__delitem__` – delete a node at a specific index
   ```python
   del linked_list[0]
   # mind that negative indexes or slices are not supported
   ```
5. `__reversed__` – return a reversed **copy** of the list
   ```python
   rev = reversed(linked_list)
   # original linked_list will remain unchanged
   # to reverse list itself, use this: linked_list.reverse()
   ```
6. `__iter__` – return a node iterator `ListNodeIterator`
   ```python
   iterator = iter(linked_list)
   node1 = next(iterator)
   node2 = next(iterator)
   ...

   # or

   for node in linked_list:
       ...
       # iterates over nodes
       # to iterate over values, use this: linked_list.values()

   ```

## ListNode

`basic_data_structure.nodes.list_node.ListNode`

If you'd like to create linked list by yourself, you can use `ListNode` class like this, for example:

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

from basic_data_structure.exceptions.list_exceptions import (
    ListHasCycleError,
    ListIndexIsNotAnIntError,
    ListIndexOfRangeError,
    ListNegativeIndexError,
    NotListNodeError,
)
from basic_data_structure.iterators.list_node_iterator import ListNodeIterator
from basic_data_structure.iterators.list_value_iterator import (
    ListValueIterator,
)
from basic_data_structure.nodes.list_node import ListNode


class LinkedList:  # noqa: WPS214 Found too many methods
    """Linked list data structure."""

    def __init__(self, *args) -> None:
        """Initialise a linked list with given sequence of elements.

        `args` could be empty, so the list will be empty at the start

        Time complexity: `O(n)` (when `n` is length of `args`)

        Parameters:
            args: a tuple of values to start with (could be empty)
        """
        self.__head = None

        previous = None
        for arg in args:
            pointer = ListNode(value=arg)
            if self.__head is None:
                self.__head = pointer
            else:
                previous.next = pointer
            previous = pointer

    def __bool__(self) -> bool:
        """Return `False` if the list is empty, `True` otherwise.

        Time complexity: `O(1)`

        Returns:
            `False` if the list is empty, `True` if there is at least one element
        """
        return self.__head is not None

    def __len__(self) -> int:
        """Return length (count of elements) of the list.

        Time complexity: `O(n)`

        Returns:
            length of the list

        Raises:
            ListHasCycleError: when the list has a cycle
        """
        length = 0

        slow = self.__head
        fast = self.__head
        while slow:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
                if fast == slow:
                    raise ListHasCycleError

            length += 1

        return length

    def __getitem__(self, index: int) -> ListNode:
        """Return a node at particular index.

        Mind that actual `ListNode` will be returned, not its value

        Time complexity: `O(n)`

        Parameters:
            index: index

        Returns:
            node at given index

        Raises:
            ListIndexOfRangeError: when there is no such index in the list
        """
        self.__validate_index(index)
        if self.__head is None:
            raise ListIndexOfRangeError

        pointer = self.__head
        idx = 0
        while pointer:
            if idx == index:
                return pointer
            pointer = pointer.next
            idx += 1

        raise ListIndexOfRangeError

    def __delitem__(self, index: int) -> None:  # noqa: WPS603 Found using restricted magic method
        """Delete a node at a specific index.

        Time complexity: `O(n)`

        Parameters:
            index: index

        Raises:
            ListIndexOfRangeError: when there is no such index in the list
        """
        self.__validate_index(index)
        if self.__head is None:
            raise ListIndexOfRangeError

        if index == 0:
            self.__head = self.__head.next
            return

        previous = None
        pointer = self.__head
        idx = 0
        while pointer:
            if idx == index:
                previous.next = pointer.next
                return
            previous = pointer
            pointer = pointer.next
            idx += 1

        raise ListIndexOfRangeError

    def __reversed__(self) -> 'LinkedList':
        """Return a reversed copy of the list.

        Time complexity: `O(n)`

        Returns:
            a reversed copy of the list

        Raises:
            ListHasCycleError: when the list has a cycle
        """
        new_list = LinkedList()
        slow = self.__head
        fast = self.__head
        while slow:
            new_list.prepend(slow.value)
            if fast and fast.next:
                fast = fast.next.next
                if slow == fast:
                    raise ListHasCycleError
            slow = slow.next
        return new_list

    def __iter__(self) -> ListNodeIterator:
        """Return nodes iterator.

        Returns:
            ListNodeIterator
        """
        return ListNodeIterator(self.__head)

    @property
    def head(self) -> Optional[ListNode]:
        """Head of the list.

        This is `@property` with `setter`, so you can assign a new `ListNode`
        to the head (or `None` to clear the list)

        ```python
        lst = LinkedList('a', 'b', 'c')
        node = lst.head  # a ListNode with value 'a' and link to next ListNode

        # this is the same as
        node = lst[0]
        ```

        Returns:
            head of the list (first node) or `None` if the list is empty
        """
        return self.__head

    @head.setter
    def head(self, new_head: Optional[ListNode]) -> None:
        """Set new head.

        Parameters:
            new_head: new ListNode to be a head of the list (or `None` to clear the list)

        Raises:
            NotListNodeError: when trying to assign not a `ListNode` or `None`
        """
        if not isinstance(new_head, (ListNode, type(None))):
            raise NotListNodeError
        self.__head = new_head

    def values(self) -> ListValueIterator:  # noqa: WPS110 Found wrong variable name
        """Return values iterator.

        On each call `next` function on the iterator, you'll be given actual value of a `ListNode`,
        not the node itself.

        If a list has a cycle, iteration over a list will be endless.

        ```python
        lst = LinkedList(1, 2, 3)

        for node in lst:
            # iterates over nodes
            print(node.value)

        for val in lst.values():
            # iterates over values
            print(val)

        ```

        Returns:
            ListValueIterator
        """
        return ListValueIterator(self.__head)

    def append(
        self,
        value: Any,  # noqa: WPS110 Found wrong variable name
    ) -> None:
        """Append value to the end of list.

        If list has a cycle, exception `ListHasCycleError` will be risen

        Time complexity: `O(n)`

        ```python
        lst = LinkedList(1, 2)
        lst.append(3)
        # 1 → 2 → 3
        ```

        Parameters:
            value: a value to append (not a `ListNode`, but actual value)

        Raises:
            ListHasCycleError: when the list has a cycle
        """
        if self.__head is None:
            self.insert(0, value)
            return

        previous = None
        pointer = self.__head
        fast_pointer = self.__head
        while pointer:
            previous = pointer
            pointer = pointer.next
            if fast_pointer and fast_pointer.next:
                fast_pointer = fast_pointer.next.next
                if fast_pointer == pointer:
                    raise ListHasCycleError

        node = ListNode(value, pointer)
        previous.next = node

    def prepend(
        self,
        value: Any,  # noqa: WPS110 Found wrong variable name
    ) -> None:
        """Prepend a value to the list (add to the beginning).

        Time complexity: `O(1)`

        ```python
        lst = LinkedList(2, 3)
        lst.prepend(1)
        # 1 → 2 → 3
        ```

        Parameters:
            value: a value to prepend (not a `ListNode`, but actual value)
        """
        self.insert(0, value)

    def insert(
        self,
        index: int,
        value: Any,  # noqa: WPS110 Found wrong variable name
    ) -> None:
        """Insert value into given index.

        Time complexity: `O(n)`

        ```python
        lst = LinkedList(1, 3)
        lst.insert(index=1, value=2)  # will insert element between 1 and 3
        lst.insert(index=100, value=4)  # will add to the end (preferably use "append" method)
        lst.insert(index=len(lst), value=5)  # will add to the end (preferably use "append" method)
        lst.insert(index=0, value=0)  # will add to the beginning (preferably use "prepend" method)
        # 0 → 1 → 2 → 3 → 4 → 5
        ```

        Parameters:
            index: a position to insert a value to (positive `int` or zero)
            value: a value to insert (not a `ListNode`, but actual value)
        """
        self.__validate_index(index)

        if index == 0 or self.__head is None:
            node = ListNode(value, self.__head)
            self.__head = node
            return

        previous = None
        pointer = self.__head
        idx = 0
        while pointer:
            previous = pointer
            pointer = pointer.next
            idx += 1
            if idx == index:
                break

        node = ListNode(value, pointer)
        previous.next = node

    def clear(self) -> None:
        """Clear the list.

        Time complexity: `O(1)`

        ```python
        lst = LinkedList('a', 'b', 'c')
        lst.clear()
        # this is the equivalent to: lst.head = None
        ```
        """
        self.__head = None

    def reverse(self) -> None:
        """Reverse the list.

        If list has a cycle, exception `ListHasCycleError` will be risen

        Time complexity: `O(n)`

        ```python
        lst = LinkedList('a', 'b', 'c', 'd', 'e')
        # before: a → b → c → d → e

        lst.reverse()
        # after: e → d → c → b → a
        ```

        Raises:
            ListHasCycleError: when the list has a cycle
        """
        if self.has_cycle():
            raise ListHasCycleError

        pointer = self.__head
        previous = None

        while pointer:
            nxt = pointer.next
            pointer.next = previous
            previous = pointer
            pointer = nxt

        self.__head = previous

    def rotate(self, count: int) -> None:  # noqa: WPS210 Found too many local variables
        """Rotate (shift) list.

        To rotate right, pass a positive value. To rotate left, pass a negative value.

        If list has a cycle, exception `ListHasCycleError` will be risen

        Time complexity: `O(n)`

        ```python
        lst = LinkedList('a', 'b', 'c', 'd', 'e')
        # a → b → c → d → e

        lst.rotate(1)
        # e → a → b → c → d

        lst.rotate(-3)
        # c → d → e → a → b
        ```

        Parameters:
            count: number of nodes to shift
        """
        if count == 0:
            return

        length = len(self)
        if length < 2:
            return

        count = count % length  # noqa: WPS350 Found usable augmented assign pattern
        if count == 0:
            return

        pointer = ListNode(None, self.__head)
        new_end = None
        idx = 0
        while pointer.next:
            if idx == length - count:
                new_end = pointer
            pointer = pointer.next
            idx += 1

        new_head = new_end.next
        new_end.next = None
        pointer.next = self.__head
        self.__head = new_head

    def has_cycle(self) -> bool:
        """Return `True` if the list has cycle, `False` otherwise.

        Time complexity: `O(n)`

        Returns:
            `True` if the list has cycle, `False` otherwise
        """
        slow = self.__head
        fast = self.__head
        while slow:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
                if fast == slow:
                    return True

        return False

    def __validate_index(self, index: int) -> None:
        """Validate "index" parameter.

        Index should be a positive int.
        Slices are not supported.
        Negative indexes are not supported.

        Parameters:
            index: a value to validate

         Raises:
             ListIndexIsNotAnIntError: when given index is not an integer (slices are not supported)
             ListNegativeIndexError: when given index is less than zero
        """
        if not isinstance(index, int):
            raise ListIndexIsNotAnIntError

        if index < 0:
            raise ListNegativeIndexError
