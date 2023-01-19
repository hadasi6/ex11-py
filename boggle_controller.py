from boggle_board_randomizer import randomize_board
from boggle_gui import BoggleGui
from boggle_model import BoggleModel

WORDS_PATH = "boggle_dict.txt"


class BoggleController:
    def __init__(self):
        self._board = randomize_board()
        self._words = BoggleController.load_words_file()
        self._model = BoggleModel(board=self._board, lst_words=self._words, reset_word=self.reset_tiles,
                                  message_setter=self.message_setter)
        self._gui = BoggleGui(board=self._board, handle_start_screen_press=self.on_start_screen_press,
                              handle_add_coordinate=self._model.add_coordinate)

    def run(self):
        self._gui.display_start_screen()
        self._gui.run()

    def on_start_screen_press(self):
        self._gui.hide_start_screen()
        self._gui.display_game_screen()

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
