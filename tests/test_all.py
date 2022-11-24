from Fprj.fprj.Works import *
import pytest


def test_get_val():
    assert get_val({"hello": "world"}, "hello") == 'world'
    assert get_val({"hello": "world"}, "hello", "python") == 'world'
    assert get_val({}, "hello", "python") == 'python'
    assert get_val({"hello": "world"}) == None
    assert get_val([2, 3], 2, 55) == None
    assert get_val({}, {5: 77}, 0) == None


@pytest.mark.parametrize('a, b, c, d', [
    ([3, 56, 77777, ], ["x", "y", "z"], 5, None)
])
def test_set_(a, b, c, d):
    assert set_(a, b, c) == d
