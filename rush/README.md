# Checkmate

This project detects whether the King is in check. It does not search for a full chess checkmate.

## Mandatory part

From the repository root:

```text
python rush/ex00/main.py
```

Output: `Success` followed by a newline.

The required function is `checkmate(board)` in `ex00/checkmate.py`. Pass a multiline string containing a square board with exactly one uppercase `K`. The function prints `Success` when an enemy attacks the King, `Fail` otherwise, and `Error` for invalid input. Importing the module does not print anything. The tutor can replace the board in `main.py`.

`P`, `B`, `R`, and `Q` represent enemy pieces. Every other character is an empty square. Pawns attack one row upward and one column left or right, as shown in the subject. Bishops attack diagonally, rooks horizontally or vertically, and queens do both. A recognized piece blocks any piece behind it. LF and CRLF line endings and a final newline are accepted; rows are not stripped because spaces count as squares.

## Bonus: board files

```text
python rush/ex01/main.py rush/ex01/valid_board.chess rush/ex01/safe_board.chess
python rush/ex01/main.py rush/ex01/invalid_board.chess rush/ex01/valid_board.chess
```

The first command prints `Success` then `Fail`. The second prints `Error` then `Success`. Missing, unreadable, invalid UTF-8, and malformed files print `Error`; processing continues with the next file. Keep `ex00` and `ex01` together because the bonus uses the mandatory implementation.

## Creative bonus: explain attacks

```text
python rush/ex01/main.py --explain rush/ex01/valid_board.chess
```

This mode displays the result, the King's coordinates, and every piece that can capture it. Coordinates start at row 1, column 1 in the top-left corner. For the sample board, the attacker is `P` at row 3, column 3. Without `--explain`, output remains one result per file.

## How the algorithm works

1. Validate the square board and locate its only King.
2. Check the two squares below the King for attacking pawns.
3. Scan outward from the King in eight directions. Stop at the first recognized piece in each direction and check whether its movement permits an attack.
4. Print the result. Every scan stops at the board edge or the first piece.

Board validation takes O(n squared) time for an n by n board. Attack detection takes O(n) time after locating the King.

Both teammates should be able to explain pawn direction, blocking, validation, and the difference between check and checkmate during the tutor evaluation. Run with `python` or `python3`; no shebang is included.
