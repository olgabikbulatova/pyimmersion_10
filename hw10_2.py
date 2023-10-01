class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = self.triangle_check(side_c)

    def triangle_check(self, side_c):
        if self.side_a < self.side_b + side_c and self.side_b < side_c + self.side_a and side_c < self.side_a + self.side_b:
            return side_c
        else:
            raise ValueError("такого треугольника не существует")

    def type_triangle(self):
        triangle = {self.side_a, self.side_b, self.side_c}
        if len(triangle) == 1:
            return f'Треугольник равносторонний'
        elif len(triangle) == 2:
            return f'Треугольник равнобедренный'
        else:
            return 'Треугольник разносторонний'

trgl = Triangle(2,2,2)
trgl1 = Triangle(2,5,4)
trgl2 = Triangle(5,5,4)
# trgl3 = Triangle(10,5,2)
for tri in [trgl, trgl1, trgl2]:
    print(tri.type_triangle())