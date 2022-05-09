import utils


def main() -> None:
    print("Dette programmet krever like mange likninger som ukjente.")
    print("Likningene kan heller ikke være identiterer og må være konsistente.")
    print("Altså kan du for eksempel ikke skrive x+y=2 og x+y=3.")
    matrix = utils.make_matrix(" ")
    solutions = matrix.solve_linear()
    utils.print_nicely_formatted(solutions, decimals=1)


if __name__ == "__main__":
    main()
