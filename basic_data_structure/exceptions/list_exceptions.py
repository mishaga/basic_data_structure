"""# List exceptions"""


class ListHasCycleError(Exception):
    """When list has cycle."""


class ListIndexOfRangeError(Exception):
    """When list index out of range."""


class ListIndexIsNotAnIntError(Exception):
    """When list index is not an integer."""


class ListNegativeIndexError(Exception):
    """When list index is negative."""


class NotListNodeError(Exception):
    """When assigning not a ListNode object."""
