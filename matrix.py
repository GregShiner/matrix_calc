import numpy as np
from typing import Tuple


class matrix(np.ndarray):
    def __init__(self, *args, **kwargs) -> None:
        self.rows = kwargs["shape"][0]
        self.columns = kwargs["shape"][1]
        super().__init__(*args, **kwargs)  # type: ignore (intellisense won't detect the arguments for ndarray.__init__)

    def __add__(self, other: "matrix") -> "matrix":
        if self.shape != other.shape:
            raise ValueError("Matrices must be of the same shape")
        new_matrix = matrix(shape=self.shape)
        # TODO: add other matrix to self and store in new_matrix
        return new_matrix
