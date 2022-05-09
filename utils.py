from typing import Iterable
from algorithm.array import Array
from algorithm.matrix import Matrix
import itertools



def make_matrix(sep: str=", ") -> Matrix:
    print(f"The separator is set to \"{sep}\"")
    first = Array(list(map(float, input("Skriv inn a, b, c ..., svar: ").split(sep))))
    res = [first]
    for _ in range(len(first) - 2):
        res.append(
            Array(list(map(float, input("Skriv inn a, b, c ..., svar: ").split(sep))))
        )
    return Matrix(res)


def letter_generator() -> Iterable[str]:
    '''A generator that starts with return value a to z, then aa to zz, aaa to zzz etc.'''
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    repeat = 1
    while True:
        for letter_tuple in itertools.product(ALPHABET, repeat=repeat):
            yield "".join(letter_tuple)
        repeat += 1


def print_nicely_formatted(values: list[float], decimals: int=2) -> None:
    print_value = f""
    for value, letter in zip(values, letter_generator()):
        print_value += f"{letter} = {round(value, decimals):.{decimals}f},\t"
    print(print_value)