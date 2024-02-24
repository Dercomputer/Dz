import pytest
from MATRIX.Matrixxx import Matrix


def test__init__1():
    m = Matrix(2, 2, [[1, 2], [2, 1]])
    assert m.lines == 2
    assert m.pillars == 2
    assert m.elements == [[1, 2], [2, 1]]


def test__init__2():
    m1 = Matrix()
    assert m1.lines == 0
    assert m1.pillars == 0
    assert m1.elements == []


def test_input_matrix1(mocker):
    mocker.patch('builtins.input', side_effect=['2', '2', '1.1 2', '2 2'])
    mtr = Matrix()
    mtr.input_matrix()
    assert mtr.lines == 2
    assert mtr.pillars == 2
    assert mtr.elements == [[1.1, 2], [2, 2]]


def test_input_matrix2(mocker):
    mocker.patch('builtins.input', side_effects=['-1', '0', '1.1', '2.2'])
    matrix = Matrix()
    with pytest.raises(ValueError):
        matrix.input_matrix()


def test_str():
    matrix = Matrix()
    assert str(matrix) == ""
