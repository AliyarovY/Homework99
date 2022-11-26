from hw100.index_of import index_of
import pytest


@pytest.mark.parametrize('a,b', [
    ([[2, 7, 3, 2, 4], 2], 0),
    (([2, 7, 3, 2, 4], 2), 0),
    (([2, 7, 3, 2, 4], 2, 2), 3),
    (([2, 7, 3, 2, 4], 7, -1), -1),
    (([2, 7, 3, 2, 4], 4, -2), 4),
    (([2, 7, 3, 2, 4], 7), 1),
    (([1, 2, 3, 2, 5], 7), -1,),
    (([1, 2, 3, 2, 5], 2, -3), 3),
])
def test_index_of(a, b):
    assert index_of(*a) == b
