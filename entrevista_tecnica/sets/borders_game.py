BLACK = 'B'
WHITE = 'W'
EMPTY = 'E'


def has_move(board, line, column):

    """
    :param board: Matrix m x n
    :param line: Linha do slot inicial
    :param column: Coluna do slot inicial
    :return: Retorna True se qualquer um dos slot estiver em Branco e forem ocupados por um jogador.
    """

    m = len(board)
    if m == 0:
        raise Exception('Taboleiro deve ter uma linha pelo menos')
    n = len(board[0])
    if n == 0:
        raise Exception('Taboleiro deve conter uma coluna pelo menos')
    color = board[line][column]
    if color == EMPTY:
        raise Exception('Posição inicial não pode ser vazia')

    def adjacents(position):
        def interval(value, value_max):
            return range(max(value - 1, 0), min(value + 2, value_max))
        p_line, p_column = position
        line_internal = interval(p_line, m)
        column_interval = interval(p_column, n)

        return [(l, c) for l in line_internal for c in column_interval]

    def has_empty_adjacent(position):
        return any(
            board[p_line][p_column] == EMPTY
            for p_line, p_column in adjacents(position)
        )

    def adjacents_with_same_color(position):
        return [(l ,c) for l, c in adjacents(position) if color == board[l][c]]

    to_be_visited = set([(line, column)])
    visited = set()

    while len(to_be_visited) > 0:
        curr_position = to_be_visited.pop()
        if has_empty_adjacent(curr_position):
            return True
        visited.add(curr_position)
        for p in adjacents_with_same_color(curr_position):
            if p not in visited:
                to_be_visited.add(p)
    return False


board_white_unfinished = [
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY]
]

board_white_finished = [
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, EMPTY]
]

print(has_move(board_white_unfinished, 1, 1))
print(has_move(board_white_finished, 1, 1))