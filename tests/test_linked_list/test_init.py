from basic_data_structure import LinkedList


def test_init_empty():
    lst = LinkedList()
    assert bool(lst) is False
    assert len(lst) == 0
    assert list(lst) == []


def test_init_one_element():
    lst = LinkedList('a')
    assert bool(lst) is True
    assert len(lst) == 1
    assert list(lst.values()) == ['a']


def test_several_elements():
    lst = LinkedList('a', 'b', 'c')
    lst.insert(len(lst), 4)
    assert bool(lst) is True
    assert len(lst) == 4
    assert list(lst.values()) == ['a', 'b', 'c', 4]
