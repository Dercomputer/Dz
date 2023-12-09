import pytest
from bfs import bfs



@pytest.mark.parametrize("graph, start, target, function, expected", [
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'A', lambda a, b: a * 2 == b,
     None),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'B', lambda a, b: a * 8 == b,
     None),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'C', lambda a, b: a == b * 3,
     None),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'D', lambda a, b: a * 5 == b * 6,
     None),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'E', lambda a, b: a == b,
     2),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'F', lambda a, b: a == b,
     2),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'G', lambda a, b: a == b,
     None),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'A', 'D', lambda a, b: a == b, 2),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'B', 'E', lambda a, b: a == b, 2),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'C', 'D', lambda a, b: 5 * a == b * 5, 1),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'D', 'E', lambda a, b: a * 2 == b * 2, 1),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'E', 'A', lambda a, b: a * 934 == b * 76, None),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'A', 'F', lambda a, b: a == b, None),
])
def test_bfs(graph, start, target, function,  expected):
    assert bfs(graph, start, target, function) == expected
