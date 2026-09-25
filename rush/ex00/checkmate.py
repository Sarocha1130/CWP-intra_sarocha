PIECES = {"K", "Q", "R", "B", "P"}


def _normalize_board(board):
    if not isinstance(board, str):
        return None

    rows = board.splitlines()

    if not rows:
        return None

    size = len(rows)

    if any(len(row) != size for row in rows):
        return None

    kings = []

    for row_index, row in enumerate(rows):
        for col_index, cell in enumerate(row):
            if cell == "K":
                kings.append((row_index, col_index))

    if len(kings) != 1:
        return None

    return rows, kings[0]


def _ray_attacks_king(
    rows,
    king_row,
    king_col,
    row_step,
    col_step,
    attackers,
):
    size = len(rows)

    row = king_row + row_step
    col = king_col + col_step

    while 0 <= row < size and 0 <= col < size:
        cell = rows[row][col]

        
        if cell in PIECES:
            return cell in attackers

        row += row_step
        col += col_step

    return False


def _is_in_check(rows, king_position):
    king_row, king_col = king_position
    size = len(rows)

    pawn_row = king_row + 1

    if pawn_row < size:
        for col_step in (-1, 1):
            pawn_col = king_col + col_step

            if (
                0 <= pawn_col < size
                and rows[pawn_row][pawn_col] == "P"
            ):
                return True

    
    directions = (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    )

    for row_step, col_step in directions:
        if _ray_attacks_king(
            rows,
            king_row,
            king_col,
            row_step,
            col_step,
            {"R", "Q"},
        ):
            return True

    
    diagonals = (
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    )

    for row_step, col_step in diagonals:
        if _ray_attacks_king(
            rows,
            king_row,
            king_col,
            row_step,
            col_step,
            {"B", "Q"},
        ):
            return True

    return False


def checkmate(board):
    parsed = _normalize_board(board)

    if parsed is None:
        print("Error")
        return

    rows, king_position = parsed

    if _is_in_check(rows, king_position):
        print("Success")
    else:
        print("Fail")