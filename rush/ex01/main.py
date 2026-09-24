import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ex00"))
from checkmate import checkmate, find_attackers, parse_board


def explain(board):
    try:
        rows, king = parse_board(board)
    except ValueError as error:
        print("Error")
        print(str(error))
        return
    attackers = find_attackers(rows, king)
    print("Success" if attackers else "Fail")
    print(f"King: row {king[0] + 1}, column {king[1] + 1}")
    if not attackers:
        print("No enemy piece can capture the King.")
    for piece, row, column in attackers:
        print(f"Attacker {piece}: row {row + 1}, column {column + 1}")


def main():
    parser = argparse.ArgumentParser(description="Check chessboard files for attacks on the King.")
    parser.add_argument("--explain", action="store_true", help="show the King and attacking pieces")
    parser.add_argument("files", nargs="*")
    arguments = parser.parse_args()
    if not arguments.files:
        print("Error")
        return
    for filename in arguments.files:
        try:
            board = Path(filename).read_text(encoding="utf-8")
        except (OSError, UnicodeError, ValueError):
            print("Error")
            continue
        if arguments.explain:
            explain(board)
        else:
            checkmate(board)


if __name__ == "__main__":
    main()
