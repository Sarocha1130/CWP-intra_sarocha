def parse_board(board):
    if not isinstance(board, str):
        raise ValueError("The board must be a string.")
    rows = board.splitlines()
    size = len(rows)
    if size == 0 or any(len(row) != size for row in rows):
        raise ValueError("The board must be a nonempty square.")
    kings = [
        (row, column)
        for row in range(size)
        for column in range(size)
        if rows[row][column] == "K"
    ]
    if len(kings) != 1:
        raise ValueError("The board must contain exactly one King.")
    return rows, kings[0]


def find_attackers(rows, king):
    size = len(rows)
    king_row, king_column = king
    attackers = []
    for column_step in (-1, 1):
        row = king_row + 1
        column = king_column + column_step
        if 0 <= row < size and 0 <= column < size:
            if rows[row][column] == "P":
                attackers.append(("P", row, column))
    directions = (
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    )
    for row_step, column_step in directions:
        row = king_row + row_step
        column = king_column + column_step
        while 0 <= row < size and 0 <= column < size:
            piece = rows[row][column]
            if piece in "PBRQK":
                diagonal = row_step != 0 and column_step != 0
                if piece == "Q" or (diagonal and piece == "B"):
                    attackers.append((piece, row, column))
                elif not diagonal and piece == "R":
                    attackers.append((piece, row, column))
                break
            row += row_step
            column += column_step
    return attackers


def checkmate(board):
    try:
        rows, king = parse_board(board)
    except ValueError:
        print("Error")
        return
    print("Success" if find_attackers(rows, king) else "Fail")
