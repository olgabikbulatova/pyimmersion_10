from random import randint


class Matrix:
    def __init__(self, columns, lines):
        self.columns = columns
        self.lines = lines
        self.data = self.matrix_data()

    def matrix_data(self):
        matrix_lst = [[randint(0, 10) for _ in range(self.columns)] for i in range(self.lines)]
        return matrix_lst

    def trans_matrix(self):
        trans_mat = [[0 for j in range(len(self.data))] for i in range(len(self.data[0]))]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                trans_mat[j][i] = self.data[i][j]
        return trans_mat


mtrx = Matrix(4,3)
print(mtrx.data)
print(mtrx.trans_matrix())

