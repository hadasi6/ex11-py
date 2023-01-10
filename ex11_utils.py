from typing import List, Tuple, Iterable, Optional
from boggle_board_randomizer import randomize_board

Board = List[List[str]]
Path = List[Tuple[int, int]]


def _is_board_coordinate(board: Board, coord: Tuple[int, int]) -> bool:
    y, x = coord
    if x < 0 or y < 0:
        return False
    board_width = len(board[0])
    board_height = len(board)
    if x >= board_width or y >= board_height:
        return False
    return True


def _is_adjacent(coord1, coord2) -> bool:
    if coord1 == coord2:
        return False  # TODO validate
    x1, y1 = coord1
    x2, y2 = coord2
    if x1 - 1 <= x2 <= x1 + 1:
        if y1 - 1 <= y2 <= y1 + 1:
            return True
    return False


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    if len(path) < 2:
        if not _is_board_coordinate(path[0]):
            return None
        y, x = path[0]
        word = board[y][x]
        if word in words:
            return word
        else:
            return None
    y, x = path[0]
    word = board[y][x]
    last_coord = path[0]
    for coord in path[1:]:
        if not _is_board_coordinate(board, coord):
            return None
        if not _is_adjacent(last_coord, coord):
            return None
        y, x = coord
        word += board[y][x]
        last_coord = coord
    if word in words:
        return word
    return None


def _matt_next_steps(board, coordinate):
    x, y = coordinate
    next_steps = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) == coordinate:
                continue
            if not _is_board_coordinate(board, (i, j)):
                continue
            next_steps.append((i, j))
    return next_steps


def _helper_find_length_n_paths(board, n, words, lst_path, path, coordinate):
    if n == 0:
        if is_valid_path(board, path, words):
            lst_path.append(path[:])
        return

    y, x = coordinate
    for next_step in _matt_next_steps(board, coordinate):
        path.append(next_step)
        _helper_find_length_n_paths(board, n - 1, words, lst_path, path, next_step)
        del path[-1]


def _cell_list(board):
    cell_lst = [(y, x) for y in range(len(board)) for x in range(len(board[0]))]
    return cell_lst


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    paths_lst = []
    if n == 0:
        return paths_lst
    for coordinate in _cell_list(board):
        _helper_find_length_n_paths(board, n - 1, words, paths_lst, [coordinate], coordinate)
    return paths_lst


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    pass


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass


board = [['T', 'M', 'V', 'W'], ['N', 'Z', 'L', 'I'], ['E', 'H', 'J', 'I'], ['T', 'O', 'T', 'S']]
words = ['MZ', 'SI']
print(find_length_n_paths(2, board, words))
