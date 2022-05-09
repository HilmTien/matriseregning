from __future__ import annotations

# kan inherite fra list men tenker at dette er bedre for å forstå klasser i utgangspunktet


class Array:
    def __init__(self, values: list[float]) -> None:
        self.values = values

    def first_elem_one(self) -> None:
        for value in self.values:
            if value:
                self.values = (self / value).values
                return

    def eliminate_value(self, reference: Array) -> None:
        for index, value in enumerate(self.values):
            if value:
                subtract_array = reference * self.values[index]
                self.values = (self - subtract_array).values
                return

    def __len__(self) -> int:
        return len(self.values)

    def __add__(self, other: Array) -> Array:
        return Array([val_1 + val_2 for val_1, val_2 in zip(self.values, other.values)])

    def __sub__(self, other: Array) -> Array:
        return Array([val_1 - val_2 for val_1, val_2 in zip(self.values, other.values)])

    def __mul__(self, constant: int) -> Array:
        return Array([val * constant for val in self.values])

    def __truediv__(self, divisor: int) -> Array:
        return Array([val / divisor for val in self.values])

    def __repr__(self) -> str:
        return f"Array({self.values})"


def main() -> None:
    a = Array([0, 1, 3])
    b = Array([0, 8, 4])

    b.eliminate_value(a)
    print(b)


if __name__ == "__main__":
    main()
