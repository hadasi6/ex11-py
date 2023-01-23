import random

from ex11_utils import is_adjacent


def randomize_feedback():
    return random.choice([
        "Good job!",
        "Very good",
        "You made me proud",
        "Dope!",
        "Amazing",
        "Wonderful",
        "Excellent",
        "Very cool"
    ])


class BoggleModel:
    def __init__(self, board, lst_words, reset_word, message_setter, score_and_words_setter):
        self._path = []
        self._temp_word = ""
        self._board = board
        self.lst_words = lst_words
        self.used_words = set()
        self.score = 0
        self._message_setter = message_setter
        self._reset_word = reset_word
        self._score_and_words_setter = score_and_words_setter

    def add_coordinate(self, coordinate):
        # Not finished writing word
        if coordinate not in self._path:
            if not self.is_valid_coordinate(coordinate):
                self._message_setter("Not adjacent!")
                self._path = []
                self._temp_word = ""
                self._reset_word()
            else:
                self._path.append(coordinate)
                self._temp_word += self._board[coordinate[0]][coordinate[1]]
                self._message_setter(self._temp_word)
        # Finished writting word
        else:
            feedback = randomize_feedback()
            self._message_setter(feedback)
            self._reset_word()

            if self.is_valid_word(self._path):
                self.used_words.add(self._temp_word)   # adding words to frame
                self._score_and_words_setter(self.score, self.used_words)

                # TODO: handle finished word
            self._path = []
            self._temp_word = ""

    def is_valid_word(self, path):  # update score
        # word = ''
        # for coord in path:
        #     char = self._board[coord[0]][coord[1]]
        #     word += char

        if not self.is_real_word(self._temp_word):
            return False
        self.score += (len(path)) ** 2
        return True

    def is_real_word(self, word) -> bool:
        if word in self.used_words:
            self._message_setter('ALREADY SELECTED!!!')
            return False
        if word not in self.lst_words:
            self._message_setter('Not a word!')
            return False
        return True

    def is_valid_coordinate(self, coordinate):
        if not self._path:
            return True
        last_coordinate = self._path[-1]
        if not is_adjacent(last_coordinate, coordinate):
            # self._message_setter("Not adjacent!")
            return False
        return True

# class Sleep:
#     def __int__(self, board, lst_words, used_words):
#         self.board = board
#         self.lst_words = lst_words
#         self.lst_used_words = used_words
#         self.score = 0
#
#     def is_valid_word(self, path):  # update score
#         word = ''
#         for coord in path:
#             char = self.board[coord[0]][coord[1]]
#             word += char
#         if not self.is_real_word(word):
#             print('ALREADY SELECTED!!!')
#             return False
#         self.score += (len(path)) ** 2
#         return True
#
#     def is_real_word(self, word) -> bool:
#         if word in self.lst_used_words:
#             return False
#         if word not in self.lst_words:
#             return False
#         return True

