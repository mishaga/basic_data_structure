from basic_data_structure import Stack


def test_init_empty():
    s = Stack()
    s.push(1)
    assert len(s) == 1


def test_init_not_empty():
    s = Stack(1, 2, 3, 4)
    s.push(5)
    assert len(s) == 5
    assert s.pop() == 5


def test_push_twice():
    s = Stack()
    s.push('a')
    s.push('b')
    assert len(s) == 2
    assert s.pop() == 'b'
