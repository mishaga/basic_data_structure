from basic_data_structure import LinkedList


def test_empty_list():
    lst = LinkedList()
    assert bool(lst) is False


def test_inited_list():
    lst = LinkedList('a', 'b', 'c')
    assert bool(lst) is True


def test_with_insert():
    lst = LinkedList()
    lst.insert(0, 'a')
    assert bool(lst) is True


def test_mix():
    lst = LinkedList(1, 2, 3)
    lst.insert(len(lst), 4)
    lst.insert(len(lst), 5)
    assert bool(lst) is True


def test_cycle(cycled_list: LinkedList):
    assert bool(cycled_list) is True
