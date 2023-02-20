import numpy as np
from operator import add


class Matrix(np.ndarray):
    def __init__(self, *args, **kwargs) -> None:
        self.rows = kwargs["shape"][0]
        self.columns = kwargs["shape"][1]
        super().__init__()  # type: ignore (intellisense won't detect the arguments for ndarray.__init__)

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.shape != other.shape:
            raise ValueError("Matrices must be of the same shape")
        new_matrix = Matrix(shape=self.shape)
        # add other matrix to self and store in new_matrix
        for i in range(self.rows):
            for j in range(self.columns):
                new_matrix[i, j] = self[i, j] + other[i, j]
        return new_matrix

    def __sub__(self, other: "Matrix") -> "Matrix":
        if self.shape != other.shape:
            raise ValueError("Matrices must be of the same shape")
        new_matrix = Matrix(shape=self.shape)
        # subtract other matrix from self and store in new_matrix
        for i in range(self.rows):
            for j in range(self.columns):
                new_matrix[i, j] = self[i, j] - other[i, j]
        return new_matrix

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.columns != other.rows:
            raise ValueError("Matrices must be of compatible shape")
        new_matrix = Matrix(shape=(self.rows, other.columns))
        # multiply self and other and store in new_matrix
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    new_matrix[i, j] += self[i, k] * other[k, j]
        return new_matrix

    def scale(self, scalar: float) -> "Matrix":
        new_matrix = Matrix(shape=self.shape)
        # multiply self by scalar and store in new_matrix
        for i in range(self.rows):
            for j in range(self.columns):
                new_matrix[i, j] = self[i, j] * scalar
        return new_matrix

    def calc_scale_row(self, row: int, scalar: float) -> list:
        return [self[row, i] * scalar for i in range(self.columns)]


    def scale_row(self, row: int, scalar: float) -> None:
        for i in range(len(self[row])):
            self[row, i] *= scalar
    
    def swap(self, row1: int, row2: int) -> None:
        self[[row1, row2]] = self[[row2, row1]]

    def add_row(
        self, row1: int, row2: int, outrow: int, scalar1: float = 1, scalar2: float = 1
    ) -> None:
        self[outrow] = list(map(add, self.calc_scale_row(row1, scalar1), self.calc_scale_row(row2, scalar2)))
