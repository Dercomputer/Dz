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


@pytest.mark.parametrize(
    ('lines', 'pillars', 'elements'),
    [
        (1, 0, [[]]),
        (0, 1, [[2, 2]]),
        (7, 3, [[2, 4, 5, 6]]),
        (0, 0, [[1.2]]),
        (1.2, 9.3, [[2, 4, 4, 5]]),
        (1, 1, [["ы"]])
    ]
)
@pytest.mark.xfail(raises=ValueError)
def test_fail_init(lines, pillars, elements):
    Matrix(lines, pillars, elements)


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
def test_init7(lines, pillars, elements):
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
        (['2 3', '2.2 3.4 2.2', '1 1 1'], 2, 3, [[2.2, 3.4, 2.2], [1, 1, 1]]),
        (['1 2', '2 2'], 1, 2, [[2, 2]])
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
        (['1 7', '2 2 2']),
        (['10 8', '2']),
        (['1 1', '2 2']),
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
        (1, 1, [[1]], '1\n'),
        (1, 2, [[2, 2]], '2 2\n'),
        (2, 3, [[2, 2, 2], [1, 1, 1]], '2 2 2\n1 1 1\n')
    ]
)
def test_str(lines, pillars, elements, result):
    assert str(Matrix(lines, pillars, elements)) == result


def test_init_3x3_1():
    m = Matrix3x3()
    assert m.pillars == 3
    assert m.lines == 3
    assert m.elements == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


@pytest.mark.parametrize(
    ('elements'),
    [
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        ([[1, 9, 0], [5, 1, 2], [6, 8, 9]]),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([[0, 0, 0], [0, 0, 0], [1, 1, 1]])
    ]
)
def test_init_3x3_2(elements):
    m = Matrix3x3(elements)
    assert m.lines == 3
    assert m.pillars == 3
    assert m.elements == elements


@pytest.mark.parametrize(
    ('side_eff'),
    [
        (['1 1 1 1', '2 2 2', '2 2 2']),
        (['1']),
        (['2 2 2 2', '2 2 2', '2 2 2 2 2 2 2']),
        (['1 1', '1 1']),
        (['1 4 6', '5 3 2', '5 3 2'])
    ]
)
@pytest.mark.xfail(raises=ValueError)
def test_input_fail(mocker, side_eff):
    mocker.patch('builtins.input', side_effects=side_eff)
    m = Matrix3x3()
    m.input_matrix3x3()


@pytest.mark.parametrize(
    ('elements', 'result'),
    [
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0),
        ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 0),
        ([[3, 4, 6], [3, 9, 3], [6, 32, 56]], 876),
        ([[-7, -4, 6], [3, 9, 3], [6, -6, -7]], -273),
        ([[9, 9, 9], [15, 15, 15], [18, 56, 78]], 0)
    ]
)
def test_determinant(elements, result):
    m = Matrix3x3(elements)
    assert m.determinant() == result


@pytest.mark.parametrize(
    ('lines', 'pillars', 'elements1', 'elements2', 'result'),
    [
        (1, 1, [[1]], [[1]], [[2]]),
        (2, 2, [[2, 2], [2, 2]], [[1, 2], [5, 4]], [[3, 4], [7, 6]]),
        (3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
         [[3, 3, 3], [3, 3, 3], [3, 3, 3]]),
        (1, 2, [[1, 2]], [[1, 2]], [[2, 4]]),
        (2, 1, [[2], [2]], [[4], [4]], [[6], [6]]),
        (1, 4, [[2, 3, 4, 5]], [[1, 1, 1, 1]], [[3, 4, 5, 6]]),
        (2, 2, [[-1, -1], [-1, -1]], [[-1, -1], [-1, -1]], [[-2, -2], [-2, -2]]),
        (1, 2, [[5.6, 2.4]], [[2.4, 5.6]], [[8.0, 8.0]])
    ]
)
def test_add(lines, pillars, elements1, elements2, result):
    assert Matrix(lines, pillars, elements1) + Matrix(lines, pillars, elements2) == Matrix(lines, pillars, result)


@pytest.mark.parametrize(
    ('lines', 'pillars', 'elements1', 'elements2', 'result'),
    [
        (1, 1, [[1]], [[1]], [[0]]),
        (2, 2, [[2, 2], [2, 2]], [[1, 2], [5, 4]], [[1, 0], [-3, -2]]),
        (3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
         [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]),
        (1, 2, [[1, 2]], [[1, 2]], [[0, 0]]),
        (2, 1, [[2], [2]], [[4], [4]], [[-2], [-2]]),
        (1, 4, [[2, 3, 4, 5]], [[1, 1, 1, 1]], [[1, 2, 3, 4]]),
        (2, 2, [[-1, -1], [-1, -1]], [[-1, -1], [-1, -1]], [[0, 0], [0, 0]]),
        (1, 1, [[-12]], [[-2]], [[-10]])
    ]
)
def test_sub(lines, pillars, elements1, elements2, result):
    assert Matrix(lines, pillars, elements1) - Matrix(lines, pillars, elements2) == Matrix(lines, pillars, result)


@pytest.mark.parametrize(
    ("lines1", "pillars1", "elements1", "lub"),
    [
        (1, 1, [[2]], 1),
        (1, 2, [[2, 1]], True),
        (2, 2, [[2, 2], [2, 2]], "ыыыыыы"),
        (1, 1, [[7]], Matrix(1, 2, [[6, 7]])),
        (1, 7, [[1, 1, 1, 1, 1, 1, 1]], 65.9),
        (1, 1, [[2]], (5, 4, 3)),
        (1, 1, [[2]], {0: "ы"})
    ]
)
@pytest.mark.xfail(raises=ValueError)
def test_fail_add(lines1, pillars1, elements1, lub):
    assert Matrix(lines1, pillars1, elements1) + lub


@pytest.mark.parametrize(
    ("lines1", "pillars1", "elements1", "lub"),
    [
        (1, 1, [[2]], 1),
        (1, 2, [[2, 1]], True),
        (2, 2, [[2, 2], [2, 2]], "ы"),
        (1, 1, [[7]], Matrix(1, 2, [[6, 7]])),
        (1, 7, [[1, 1, 1, 1, 1, 1, 1]], 65.9),
        (1, 1, [[2]], (5, 4, 3)),
        (1, 1, [[2]], {0: "ы"})
    ]
)
@pytest.mark.xfail(raises=ValueError)
def test_fail_sub(lines1, pillars1, elements1, lub):
    assert Matrix(lines1, pillars1, elements1) - lub


@pytest.mark.parametrize(
    ('lines', 'pillars', 'elements', 'elements2', 'result'),
    [
        (1, 1, [[2]], [[6]], True),
        (2, 1, [[2], [2]], [[2], [2]], False),
        (2, 1, [[2], [2]], [[2], [2]], "ы"),
        (2, 1, [[2], [2]], [[2], [2]], None),
        (1, 1, [[2]], [[6]], 9)
    ]
)
@pytest.mark.xfail(raises=ValueError)
def test_fail_eq_matrix_add(lines, pillars, elements, elements2, result):
    assert Matrix(lines, pillars, elements) + Matrix(lines, pillars, elements2) == result


@pytest.mark.parametrize(
    ('lines', 'pillars', 'elements', 'elements2', 'result'),
    [
        (1, 1, [[2]], [[6]], True),
        (2, 1, [[2], [2]], [[2], [2]], False),
        (2, 1, [[2], [2]], [[2], [2]], "ы"),
        (2, 1, [[2], [2]], [[2], [2]], None),
        (1, 1, [[2]], [[6]], 9)
    ]
)
@pytest.mark.xfail(raises=ValueError)
def test_fail_eq_matrix_sub(lines, pillars, elements, elements2, result):
    assert Matrix(lines, pillars, elements) - Matrix(lines, pillars, elements2) == result


@pytest.mark.parametrize(
    ('lines', 'pillars', 'elements', 'other'),
    [
        (1, 1, [[6]], "ы"),
        (1, 1, [[2]], None),
        (2, 2, [[2, 2], [3, 3]], {0: "ы"}),
        (1, 1, [[5]], True),
        (1, 1, [[2]], [[2]])
    ]
)
@pytest.mark.xfail(raises=ValueError)
def test_fail_eq(lines, pillars, elements, other):
    assert Matrix(lines, pillars, elements) == other


def test_ne():
    assert Matrix(1, 1, [[2]]) != Matrix(1, 1, [[3]])


def test_eq():
    assert Matrix(1, 1, [[2]]) == Matrix(1, 1, [[2]])
    assert Matrix(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == Matrix3x3([[1, 1, 1], [1, 1, 1], [1, 1, 1]])


@pytest.mark.parametrize(
    ("elements1", "elements2", "result"),
    [
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]]),
        ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]], [[4, 4, 4], [4, 4, 4], [4, 4, 4]])
    ]
)
def test_add_3x3(elements1, elements2, result):
    assert Matrix3x3(elements1) + Matrix3x3(elements2) == Matrix3x3(result)


@pytest.mark.parametrize(
    ("elements1", "elements2", "result"),
    [
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    ]
)
def test_sub_3x3(elements1, elements2, result):
    assert Matrix3x3(elements1) - Matrix3x3(elements2) == Matrix3x3(result)


def test_eq_3x3():
    assert Matrix3x3([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == Matrix3x3([[1, 1, 1], [1, 1, 1], [1, 1, 1]])


def test_ne_3x3():
    assert Matrix3x3([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) != Matrix3x3([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
