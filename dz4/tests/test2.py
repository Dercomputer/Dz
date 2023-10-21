import pytest
from dz4.task2 import factorial
@pytest.mark.parametrize(
    ('n', 'a'),
    [
        (1, 1)
        (-1, 1)
        (0, 1)
        (5, 120)
    ]
)
def test(n, a):
    assert factorial(n) == a