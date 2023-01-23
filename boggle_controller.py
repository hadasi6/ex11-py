from boggle_board_randomizer import randomize_board
from boggle_gui import BoggleGui
from boggle_model import BoggleModel

WORDS_PATH = "boggle_dict.txt"


class BoggleController:
    def __init__(self):
        self._board = randomize_board()
        self._words = BoggleController.load_words_file()
        self._model = BoggleModel(board=self._board, lst_words=self._words,
                                  reset_word=self.reset_tiles,
                                  message_setter=self.message_setter,
                                  score_and_words_setter=None)
        self._gui = BoggleGui(handle_start_screen_press=self.start_game,
                              handle_add_coordinate=self._model.add_coordinate,
                              handle_time_out=self.game_over,
                              handle_restart=self.restart_game)
        self._gui.set_board(self._board)

    def run(self):
        self._gui.display_start_screen()
        self._gui.run()

    def start_game(self):
        self._gui.hide_start_screen()
        self._gui.display_game_screen()
        self._model._score_and_words_setter = self._gui.game_screen.set_score_and_words

    @staticmethod
    def load_words_file():
        with open(WORDS_PATH, 'r') as fp:
            return fp.read().splitlines()

    def new_board(self):
        self._board = randomize_board()

    def message_setter(self, message):
        self._gui.set_message(message)

    def reset_tiles(self):
        self._gui.game_screen.reset_tiles()

    def game_over(self):
        self._gui.hide_game_screen()
        self._gui.end_screen.message = \
            f"Game over! Your score: {self._model.score}"
        self._gui.display_end_screen()

    def restart_game(self):
        self._board = randomize_board()
        self._model = BoggleModel(board=self._board, lst_words=self._words, reset_word=self.reset_tiles,
                                  message_setter=self.message_setter,
                                  score_and_words_setter=None)

        self._gui.set_add_coordinate_handler(self._model.add_coordinate)
        self._gui.set_board(self._board)

        self._gui.hide_end_screen()
        self._gui.display_game_screen()
        self._model._score_and_words_setter = self._gui.game_screen.set_score_and_words

