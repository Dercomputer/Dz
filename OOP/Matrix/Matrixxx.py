class Matrix:

    def __init__(self, lines: int = 0, pillars: int = 0, elements: list = None):
        if elements is None:
            elements = []
        self.lines = lines
        self.pillars = pillars
        self.elements = elements
        self.__correct()

    def __correct(self):
        for i in range(len(self.elements)):
            if len(self.elements[i]) != self.pillars:
                raise ValueError("Так матрицу никто не вводит")

    def __str__(self):
        output = ''
        for j in range(self.lines):
            output += ' '.join(str(i) for i in self.elements[j]) + '\n'
        return output

    def _size_matrix(self):
        while True:
            try:
                self.lines, self.pillars = map(int, input("Введите количество строк и столбцов: ").split())
            except ValueError:
                continue
            else:
                break

    def _matrix_elements(self):
        self.elements = []
        for i in range(self.lines):
            self.elements.append(list(map(float, input(f"string: ").split())))
            self.__correct()

    def input_matrix(self):
        self._size_matrix()
        self._matrix_elements()

    # def __add__(self, b):
    #     for i in range(self.lines):
    #         print(self.elements[i])


class Matrix3x3(Matrix):

    def __init__(self, elements: list = None):
        if elements is None:
            elements = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        super().__init__(3, 3, elements)

    def input_matrix(self):
        super()._matrix_elements()

    def determinant(self):
        return self.elements[0][0] * self.elements[1][1] * self.elements[2][2] + self.elements[0][1] \
            * self.elements[1][2] * self.elements[2][0] + self.elements[0][2] * self.elements[1][0]  \
            * self.elements[2][1] - self.elements[0][2] * self.elements[1][1] * self.elements[2][0]  \
            - self.elements[0][0] * self.elements[1][2] * self.elements[2][1] - self.elements[1][0]  \
            * self.elements[0][1] * self.elements[2][2]


if __name__ == "__main__":
    #     #n1 = Matrix(2, 2, [[1, 1], [1, 1]])
    #     #n2 = Matrix(2, 2, [[1, 1], [1, 1]])
    #     #print(n1 + n2)
    p = Matrix3x3()
    p.input_matrix()
    print(p.determinant())



# m = PMatrix(2, 2, [1, 1, 1, 1])
# print(m)
