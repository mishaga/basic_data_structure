from basic_data_structure import Stack


def test_empty_stack():
    s = Stack()
    assert bool(s) is False


def test_inited_stack():
    s = Stack('a')
    assert bool(s) is True


def test_pushed_stack():
    s = Stack()
    s.push(0)
    assert bool(s) is True


def test_mix():
    s = Stack(1, 2, 3)
    s.push(4)
    s.push(5)
    assert bool(s) is True


def test_clear():
    s = Stack(1, 2, 3)
    s.push(4)
    s.push(5)
    s.clear()
    assert bool(s) is False
