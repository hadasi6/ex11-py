import tkinter as tki

from end_screen_gui import EndScreenGui
from game_screen_gui import GameScreenGui
from start_screen_gui import StartScreenGui

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
TOP_BAR_HEIGHT = 60
BOTTOM_BAR_HEIGHT = 60


class BoggleGui:
    def __init__(self, handle_start_screen_press, handle_add_coordinate, handle_time_out, handle_restart):
        self._create_root()
        self.start_screen = None
        self.game_screen = None
        self._handle_start_screen_press = handle_start_screen_press
        self._handle_add_coordinate = handle_add_coordinate
        self._board = None
        self._handle_time_out = handle_time_out
        self._handle_restart = handle_restart

        self.end_screen = EndScreenGui(handle_play_again=self.restart_game)

    def set_add_coordinate_handler(self, handler):
        self._handle_add_coordinate = handler

    def set_board(self, board):
        self._board = board

    def _create_root(self):
        root = tki.Tk()
        root.geometry(f"{CANVAS_WIDTH}x{CANVAS_WIDTH}")
        root.configure()
        root.resizable(False, False)  # Disable window resize
        root.title("Boggle")  # Set window title
        self._root = root

    def run(self):
        self._root.mainloop()

    def set_message(self, message):
        self.game_screen.set_message(message)

    def display_start_screen(self):
        self.start_screen = StartScreenGui(self._root, self._handle_start_screen_press)
        self.start_screen.create()

    def hide_start_screen(self):
        self.start_screen.destroy()

    def display_game_screen(self):
        self.game_screen = GameScreenGui(self._root, self._board, self._handle_add_coordinate, self._handle_time_out)
        self.game_screen.create()

    def hide_game_screen(self):
        self.game_screen.destroy()

    def display_end_screen(self):
        self.end_screen.create()

    def hide_end_screen(self):
        self.end_screen.destroy()

    def restart_game(self):
        self.game_screen.reset_score_and_words()
        self._handle_restart()
