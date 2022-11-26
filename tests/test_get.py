from hw100.get import get
import pytest


@pytest.mark.parametrize('a,b,c,d', [
    ([1, 2, 3], 1, "a", 2),
    ([4, 5, 6], 7, "val", 'val')
])
def test_get(a, b, c, d):
    assert get(a, b, c) == d

