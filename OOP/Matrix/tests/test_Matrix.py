import pytest
from MATRIX.Matrixxx import Matrix, Matrix3x3


@pytest.fixture()
def matrix():
    return Matrix(2, 2, [[1, 2], [2, 1]])


def test__init__1(matrix):
    assert matrix.lines == 2
    assert matrix.pillars == 2
    assert matrix.elements == [[1, 2], [2, 1]]


def test__init__2():
    m1 = Matrix()
    assert m1.lines == 0
    assert m1.pillars == 0
    assert m1.elements == []


def test_input_matrix1(mocker):
    mocker.patch('builtins.input', side_effect=['2 2', '1.1 2', '2 2'])
    mtr = Matrix()
    mtr.input_matrix()
    assert mtr.lines == 2
    assert mtr.pillars == 2
    assert mtr.elements == [[1.1, 2], [2, 2]]


@pytest.mark.xfail(raises=ValueError)
def test_much_el(mocker):
    mocker.patch('builtins.input', side_effect=['2 3', '1 2 3', '4 5 6 7'])
    matrix = Matrix()
    matrix.input_matrix()


def test_str():
    matrix = Matrix()
    assert str(matrix) == ""


def test_init_():
    m = Matrix3x3()
    assert m.pillars == 3
    assert m.lines == 3
    assert m.elements == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_determinant(mocker):
    mocker.patch('builtins.input', side_effects=['1 1 1', '1 1 1', '1 1 1'])
    matrix = Matrix3x3()
    assert matrix.determinant() == 0


@pytest.mark.xfail(raises=ValueError)
def test_input(mocker):
    mocker.patch('builtins.input', side_effects=['1 1 1 1', '2 2 2', '2 2 2'])
    matrix = Matrix3x3()
    matrix.input_matrix()
