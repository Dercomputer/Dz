class Matrix:

    def __init__(self, lines: int = 0, pillars: int = 0, elements: list = []):
        self.lines = lines
        self.pillars = pillars
        self.elements = elements

    def __str__(self):
        output = ''
        for j in range(self.lines):
            output += ' '.join(str(i) for i in self.elements[j]) + '\n'
        return output

    def input_matrix(self):
        self.lines, self.pillars = int(input("Count lines: ")), int(input("Count pillars: "))
        if self.lines < 0 or self.pillars < 0:
            raise ValueError
        for i in range(self.lines):
            self.elements.append(list(map(float, input(f"string {i + 1}: ").split())))
            if len(self.elements[i]) != self.pillars:
                raise ValueError("НЕКОРРЕКТНЫЙ ВВОД")
            for j in range(self.pillars):
                if self.elements[i][j] % 1 == 0:
                    self.elements[i][j] = int(self.elements[i][j])


class Matrix3x3(Matrix):
    pass


if __name__ == "__main__":
    n = Matrix()
    n.input_matrix()
    print(n)
