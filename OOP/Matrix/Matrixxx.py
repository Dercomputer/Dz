class Matrix:

    def __init__(self, lines: int = 0, pillars: int = 0, elements: list = None):
        if elements is None:
            elements = []
        self.lines = lines
        self.pillars = pillars
        self.elements = elements
        self._correctinit()

    def __correct(self):
        self._correctnumber()
        self._correctelements()

    def _correctnumber(self):
        if self.lines != 0 and self.pillars == 0 or self.lines == 0 and self.pillars != 0:
            raise ValueError("Количество столбцов или строк не может быть нулевым")
        if self.lines < 0 or self.pillars < 0:
            raise ValueError("Число строк или столбцов не может быть отрицательным")

    def _correctelements(self):
        for i in range(len(self.elements)):
            if len(self.elements[i]) != self.pillars:
                raise ValueError("Число элементов в строке должно совпадать с числом столбцов")

    def _correctinit(self):
        for i in range(len(self.elements)):
            for j in range(len(self.elements[i])):
                if isinstance(self.elements[i][j], int) is False and isinstance(self.elements[i][j], float) is False:
                    raise ValueError("В матрицу подают только числа")
        self.__correct()

    def __str__(self):
        output = ''
        for j in range(self.lines):
            output += ' '.join(str(i) for i in self.elements[j]) + '\n'
        return output

    def _size_matrix(self):
        while True:
            try:
                self.lines, self.pillars = map(int, input("Введите количество строк и столбцов: ").split())
                self._correctnumber()
            except ValueError:
                continue
            else:
                break

    def _matrix_elements(self):
        self.elements = []
        for i in range(self.lines):
            self.elements.append(list(map(float, input(f"string: ").split())))
            self._correctelements()
        if len(self.elements) != self.lines and self.elements != [[]]:
            raise ValueError("Число элементов больше числа строк")

    def input_matrix(self):
        self._size_matrix()
        self._matrix_elements()

    def __plus(self, other):
        new_elements = []
        for i in range(self.lines):
            new_lines = []
            for j in range(self.pillars):
                new_lines.append(self.elements[i][j] + other.elements[i][j])
            new_elements.append(new_lines)
        if isinstance(self, Matrix):
            return Matrix(self.lines, self.pillars, new_elements)
        elif isinstance(self, Matrix3x3):
            return Matrix3x3(new_elements)

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.pillars == other.pillars and self.lines == other.lines:
                return self.__plus(other)
            else:
                raise ValueError("Нельзя складывать разные по форме матрицы")
        else:
            raise ValueError("Это нельзя складывать")

    def __minus(self, other):
        new_elements = []
        for i in range(self.lines):
            new_lines = []
            for j in range(self.pillars):
                new_lines.append(self.elements[i][j] - other.elements[i][j])
            new_elements.append(new_lines)
        if isinstance(self, Matrix):
            return Matrix(self.lines, self.pillars, new_elements)
        elif isinstance(self, Matrix3x3):
            return Matrix3x3(new_elements)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.pillars == other.pillars and self.lines == other.lines:
                return self.__minus(other)
            else:
                raise ValueError("Нельзя вычитать разные по форме матрицы")
        else:
            raise ValueError("Это нельзя вычитать")

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.elements == other.elements
        else:
            raise ValueError("Нельзя сравнить")

    def __ne__(self, other):
        if isinstance(other, Matrix):
            return self.elements != other.elements
        else:
            raise ValueError("Нельзя сравнить")


class Matrix3x3(Matrix):

    def __init__(self, elements: list = None):
        if elements is None:
            elements = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        super().__init__(3, 3, elements)

    def input_matrix3x3(self):
        super()._matrix_elements()

    def determinant(self):
        return self.elements[0][0] * self.elements[1][1] * self.elements[2][2] + self.elements[0][1] \
            * self.elements[1][2] * self.elements[2][0] + self.elements[0][2] * self.elements[1][0] \
            * self.elements[2][1] - self.elements[0][2] * self.elements[1][1] * self.elements[2][0] \
            - self.elements[0][0] * self.elements[1][2] * self.elements[2][1] - self.elements[1][0] \
            * self.elements[0][1] * self.elements[2][2]


if __name__ == "__main__":
    n1 = Matrix(2, 2, [[1, 1], [1, 1]])
    n2 = Matrix(2, 2, [[1, 1], [1, 1]])
    n3 = Matrix(1, 1, [[1]])
    print(n1 - n2)
    m = Matrix3x3()
    m.input_matrix3x3()
    print(m.elements)
    # print(p.elements)
    # m = Matrix()
    # m.input_matrix()
