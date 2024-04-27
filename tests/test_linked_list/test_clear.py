import pytest

from basic_data_structure import LinkedList


@pytest.mark.parametrize('list_name', (
    'int_list',
    'str_list',
    'cycled_list',
))
def test_clear(list_name: str, request: pytest.FixtureRequest):
    lst: LinkedList = request.getfixturevalue(list_name)
    lst.clear()
    assert bool(lst) is False
    assert len(lst) == 0
    assert list(lst) == []
    assert lst.has_cycle() is False
