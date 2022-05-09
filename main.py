import utils


def main() -> None:
    print("Dette programmet krever like mange likninger som ukjente.")
    print("Likningene kan heller ikke være identiterer og må være konsistente.")
    print("Altså kan du for eksempel ikke skrive x+y=2 og x+y=3.")
    matrix = utils.make_matrix()
    print(matrix)
    print(matrix.solve_linear())


if __name__ == "__main__":
    main()
