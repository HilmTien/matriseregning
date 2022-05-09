from algorithm.array import Array
from algorithm.matrix import Matrix


def make_matrix(sep: str=", ") -> Matrix:
    print(f"The separator is set to \"{sep}\"")
    first = Array(list(map(float, input("Skriv inn a, b, c ..., svar: ").split(sep))))
    res = [first]
    for _ in range(len(first) - 2):
        res.append(
            Array(list(map(float, input("Skriv inn a, b, c ..., svar: ").split(sep))))
        )
    return Matrix(res)
