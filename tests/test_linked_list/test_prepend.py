from basic_data_structure import LinkedList


def test_empty_list(empty_list: LinkedList):
    empty_list.prepend('a')
    assert list(empty_list.values()) == ['a']


def test_not_empty(str_list: LinkedList):
    str_list.prepend('zero')
    assert list(str_list.values()) == ['zero', 'a', 'b', 'c']
