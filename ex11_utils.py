from typing import List, Tuple, Iterable, Optional, Dict
from functools import reduce
from sortedcontainers import SortedList

import boggle_board_randomizer
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


def is_adjacent(coord1: Tuple[int, int], coord2: Tuple[int, int]) -> bool:
    if coord1 == coord2:
        return False  # TODO validate
    x1, y1 = coord1
    x2, y2 = coord2
    if x1 - 1 <= x2 <= x1 + 1:
        if y1 - 1 <= y2 <= y1 + 1:
            return True
    return False


def is_valid_path(board: Board, path: Path, 
                words: Iterable[str]) -> Optional[str]:
    if not path:
        return None
    if len(path) < 2:
        if not _is_board_coordinate(board, path[0]):
            return None
        y, x = path[0]
        word = board[y][x]
        if word in words:
            return word
        else:
            return None
    if not _is_board_coordinate(board, path[0]):
        return None
    y, x = path[0]
    word = board[y][x]
    last_coord = path[0]
    for coord in path[1:]:
        if not _is_board_coordinate(board, coord):
            return None
        if not is_adjacent(last_coord, coord):
            return None
        y, x = coord
        word += board[y][x]
        last_coord = coord
    if word in words:
        return word
    return None


def _matt_next_steps(board: Board, coordinate: Tuple[int, int], 
                    path: Path) -> Iterable[Tuple[int, int]]:
    x, y = coordinate
    next_steps = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) == coordinate:
                continue
            if not _is_board_coordinate(board, (i, j)):
                continue
            if (i, j) in path:
                continue
            next_steps.append((i, j))
    return next_steps


def _helper_find_length_n_paths(board: Board, n: int, words: List[str], 
                            lst_path: List[Path], path: Path, 
                            coordinate: Tuple[int, int]):
    if n == 0:
        if is_valid_path(board, path, words):
            lst_path.append(path[:])
        return

    for next_step in _matt_next_steps(board, coordinate, path):
        path.append(next_step)
        _helper_find_length_n_paths(board, n - 1, words, lst_path, path, next_step)
        del path[-1]


def _cell_list(board: Board) -> List[Tuple[int, int]]:
    cell_lst = [(y, x) for y in range(len(board)) for x in range(len(board[0]))]
    return cell_lst


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    # No path can be longer than the number of cells
    if n > _number_of_cells(board):
        return []
    path_lst = []
    for coordinate in _cell_list(board):
        _helper_find_length_n_paths(board, n - 1, words, path_lst, [coordinate], coordinate)
    return path_lst


def _helper_find_length_n_words(n: int, board: Board, words: Iterable[str], 
                            temp_word: str, lst_path: List[Path], path: Path, 
                            coordinate: Tuple[int, int]):
    if len(temp_word) > n:
        return
    elif len(temp_word) == n:
        if temp_word in words:
            lst_path.append(path[:])
            return

    for next_step in _matt_next_steps(board, coordinate, path):
        path.append(next_step)
        tile = board[next_step[0]][next_step[1]]
        next_word = temp_word + tile
        _helper_find_length_n_words(n, board, words, next_word, lst_path, path, next_step)
        del path[-1]


def _number_of_cells(board: Board):
    return len(board) * len(board[0])


def _get_max_tile_length(board: Board):
    tile_lengths = [len(tile) for row in board for tile in row]
    return reduce(max, tile_lengths)


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    if n > _get_max_tile_length(board) * _number_of_cells(board):
        return []
    path_lst = []
    for coordinate in _cell_list(board):
        y, x = coordinate
        _helper_find_length_n_words(n, board, words, board[y][x], path_lst, [coordinate], coordinate)
    return path_lst


# def max_word_length(words: Iterable[str]) -> int:
#     return reduce(max, [len(w) for w in words])


def _is_word_start(temp_word: str, sorted_words: SortedList):
    letter = temp_word[-1]
    next_letter = chr(ord(letter) + 1)
    next_word = temp_word[:-1] + next_letter
    start = sorted_words.bisect_left(temp_word)
    end = sorted_words.bisect_right(next_word)

    if start == end:
        return False
    elif end - start == 1:
        return sorted_words[start].startswith(temp_word)
    else:
        return True


def _helper_max_score_paths(board: Board, words: Iterable[str], temp_word: str, word_scores: Dict[str, Path],
                            path: Path, coordinate: Tuple[int, int]):
    if len(path) > _number_of_cells(board):
        return
    if temp_word in words:
        if temp_word in word_scores:
            if len(path) > len(word_scores[temp_word]):
                word_scores[temp_word] = path[:]
        else:
            word_scores[temp_word] = path[:]
    elif not _is_word_start(temp_word, words):
        return

    for next_step in _matt_next_steps(board, coordinate, path):
        path.append(next_step)
        tile = board[next_step[0]][next_step[1]]
        next_word = temp_word + tile
        _helper_max_score_paths(board, words, next_word, word_scores, path, next_step)
        del path[-1]


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    word_scores = {}
    sorted_words = SortedList(words) # O(nlog(n))
    for coordinate in _cell_list(board):
        y, x = coordinate
        _helper_max_score_paths(board, sorted_words, board[y][x], word_scores, [coordinate], coordinate)
    return list(word_scores.values())


if __name__ == "__main__":
    board = [['T', 'M', 'V', 'W'], ['N', 'Z', 'S', 'I'], ['E', 'H', 'J', 'I'], ['T', 'O', 'T', 'IS']]
    words = set(['MZ', 'SI', 'DSUETT', 'IS', 'IIS', 'TIS', 'T', 'W', 'TIIS'])
    print(max_score_paths(board, words))
    # paths = find_length_n_words(5, board, words)
    # print(len(paths))
    # print(paths)
    # print(*(is_valid_path(board, p, words) for p in paths))
    # for lst in paths:
    #     fun = reduce(lambda x, lst: x[tuple(y)]=. and
    # for i in range(len(paths)):
    #     lst = paths[i]
    #     if any((lst == lst2 for j, lst2 in enumerate(paths) if i != j)):
    #         print(lst, is_valid_path(board, lst, words))
    board = boggle_board_randomizer.randomize_board()
    with open('boggle_dict.txt', 'r', newline='') as fp:
        words = fp.read().splitlines()
    print("Finding words with real dict:")
    print(max_score_paths(board, words))

