import pytest
from Matrixxx import Matrix


def test__init__():
    m = Matrix(2, 2, [[1, 2], [2, 1]])
    assert m.lines == 2
    assert m.pillars == 2
    assert m.elements == [[1, 2], [2, 1]]
    m1 = Matrix()
    assert m1.lines == 0
    assert m1.pillars == 0
    assert m1.elements == []


def test_input_matrix(mocker):
    mocker.patch('builtins.input', side_effect=['2', '2', '1.1 2', '2 2'])
    mtr = Matrix()
    mtr.input_matrix()
    assert mtr.lines == 2
    assert mtr.pillars == 2
    assert mtr.elements == [[1.1, 2], [2, 2]]
    mocker.patch('builtins.input', side_effects=['-1', '0', '1.1', '2.2'])
    matrix = Matrix()
    with pytest.raises(ValueError):
        matrix.input_matrix()

@pytest.mark.parametrize(
    ('lines', 'pillars', 'elements', 'output'),
    [
        (2, 2, [[1, 1], [2, 2]], '1 1\n2 2\n'),
        (2, 4, [[1, 1, 4, 2], [2, 2, 0, 0]], '1 1 4 2\n2 2 0 0\n'),
    ]
)


def test__str__(lines, pillars, elements, output):
    assert Matrix.__str__(Matrix(lines, pillars, elements)) == output
