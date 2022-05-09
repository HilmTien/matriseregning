from .array import Array
import copy


class Matrix:
    def __init__(self, matrix: list[Array]) -> None:
        self.grid = matrix

    def solve_linear(self) -> list[int]:
        grid = copy.deepcopy(self.grid)
        # Using elimination method

        # Making the staircase
        for index, equation in enumerate(grid):
            grid[index].first_elem_one()
            for i, eq in enumerate(grid[index + 1 :], index + 1):
                grid[i].eliminate_value(grid[index])

        print(grid)

    def size(self) -> tuple[int, int]:
        return (len(self.grid), len(self.grid[0]))

    def __repr__(self) -> str:
        return f"Matrix({self.grid})"
