from .array import Array
import copy


class Matrix:
    def __init__(self, matrix: list[Array]) -> None:
        self.grid = matrix

    def solve_linear(self) -> list[float]:
        grid = copy.deepcopy(self.grid)
        # Using elimination method

        # Making the staircase
        for index, equation in enumerate(grid):
            grid[index].first_elem_one()
            for i, eq in enumerate(grid[index + 1 :], index + 1):
                grid[i].eliminate_value(grid[index])

        # Reducing matrix to isolate coefficients
        for index in range(len(grid) - 1, 0, -1):
            for i in range(index):
                grid[i] -= grid[index] * grid[i].values[index]
        
        # Return values
        return [equation.values[-1] for equation in grid]

    def size(self) -> tuple[int, int]:
        return (len(self.grid), len(self.grid[0]))

    def __repr__(self) -> str:
        return f"Matrix({self.grid})"
