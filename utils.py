from algorithm.array import Array
from algorithm.matrix import Matrix


def make_matrix() -> Matrix:
    first = Array(list(map(float, input("Skriv inn a, b, c ..., svar: ").split(", "))))
    res = [first]
    for _ in range(len(first) - 2):
        res.append(
            Array(list(map(float, input("Skriv inn a, b, c ..., svar: ").split(", "))))
        )
    return Matrix(res)
