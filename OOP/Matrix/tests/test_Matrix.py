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


@pytest.mark.xfail(raises=ValueError)
def test_fail_init():
    m = Matrix(1, 0, [[]])


@pytest.mark.parametrize(
    ('lines', 'pillars', 'elements'),
    [
        (2, 2, [[2, 2], [2, 2]]),
        (5, 5, [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]),
        (1, 1, [[2]]),
        (3, 3, [[3, 3, 3], [3, 3, 3], [3, 3, 3]]),
        (2, 2, [[1, 2], [2, 2]]),
        (4, 4, [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]),
        (0, 0, [[]]),
        (2, 3, [[2, 2, 2], [2, 2, 2]]),
        (4, 1, [[1], [2], [3], [3]])
    ]
)
def test_init(lines, pillars, elements):
    m = Matrix(lines, pillars, elements)
    assert m.lines == lines
    assert m.pillars == pillars
    assert m.elements == elements


def test_input_matrix1(mocker):
    mocker.patch('builtins.input', side_effect=['2 2', '1.1 2', '2 2'])
    mtr = Matrix()
    mtr.input_matrix()
    assert mtr.lines == 2
    assert mtr.pillars == 2
    assert mtr.elements == [[1.1, 2], [2, 2]]


@pytest.mark.parametrize(
    ('side_effects', 'lines', 'pillars', 'elements'),
    [
        (['2 2', '1.1 2', '2 2'], 2, 2, [[1.1, 2], [2, 2]]),
        (['3 3', '3 3 3', '3 3 3', '3 3 3'], 3, 3, [[3, 3, 3], [3, 3, 3], [3, 3, 3]]),
        (['1 1', '2'], 1, 1, [[2]]),
        (['2 3', '2.2 3.4 2.2', '1 1 1'], 2, 3, [[2.2, 3.4, 2.2], [1, 1, 1]])
    ]
)
def test_input_matrix2(mocker, side_effects, lines, pillars, elements):
    mocker.patch('builtins.input', side_effect=side_effects)
    mtr = Matrix()
    mtr.input_matrix()
    assert mtr.lines == lines
    assert mtr.pillars == pillars
    assert mtr.elements == elements


@pytest.mark.parametrize(
    ("side_effects"),
    [
        (['2 3', '1 2 3', '4 5 6 7']),
        (['2 2', '2 2 2', '2']),
        (['1 1', '2 2']),
        (['1 7', '2 2 2'])
    ]
)
@pytest.mark.xfail(raises=ValueError)
def test_much_el(mocker, side_effects):
    mocker.patch('builtins.input', side_effect=side_effects)
    matrix = Matrix()
    matrix.input_matrix()


@pytest.mark.parametrize(
    ('lines', 'pillars', 'elements', 'result'),
    [
        (0, 0, [[]], ''),
        (2, 2, [[2, 2], [2, 2]], '2 2\n2 2\n'),
        (1, 1, [[1]], '1\n')
    ]
)
def test_str(lines, pillars, elements, result):
    assert str(Matrix(lines, pillars, elements)) == result


def test_init_():
    m = Matrix3x3()
    assert m.pillars == 3
    assert m.lines == 3
    assert m.elements == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


@pytest.mark.parametrize(
    ('side_ef', 'result'),
    [
        (['1 1 1', '1 1 1', '1 1 1'], 0),
        (['1 1 1', '0 0 0', '1 1 1'], 0)
    ]
)
def test_determinantinput(mocker, side_ef, result):
    mocker.patch('builtins.input', side_effects=side_ef)
    matrix = Matrix3x3()
    assert matrix.determinant() == result


@pytest.mark.parametrize(
    ('elements', 'result'),
    [
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0),
        ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 0)
    ]
)
def test_determinant(elements, result):
    m = Matrix3x3(elements)
    assert m.determinant() == result


@pytest.mark.parametrize(
    ('side_eff'),
    [
        ('1 1 1 1', '2 2 2', '2 2 2'),
        ('1'),
        ('2 2 2 2', '2 2 2', '2 2 2 2 2 2 2')
    ]
)
@pytest.mark.xfail(raises=ValueError)
def test_input(mocker, side_eff):
    mocker.patch('builtins.input', side_effects=side_eff)
    matrix = Matrix3x3()
    matrix.input_matrix()
