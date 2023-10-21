import pytest
from dz4.task3 import unik
@pytest.mark.parametrize(
    ('n',),
    [
        [11, 23, 66]
        [1242525515125]
        ["qaa", "2424", "qaq"]
        (5, 120)
    ]
)
def test(n):
    assert unik(n) is True