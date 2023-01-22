import tkinter as tki

from game_screen_gui import GameScreenGui
from start_screen_gui import StartScreenGui

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
TOP_BAR_HEIGHT = 60
BOTTOM_BAR_HEIGHT = 60


class BoggleGui:
    def __init__(self, board, handle_start_screen_press, handle_add_coordinate):
        self._create_root()
        self._start_screen = StartScreenGui(self._root, handle_start_screen_press)
        self._handle_start_screen_press = handle_start_screen_press
        self._handle_add_coordinate = handle_add_coordinate
        self._board = board
        self.game_screen = GameScreenGui(board, self._root, handle_add_coordinate)

    def _create_root(self):
        root = tki.Tk()
        root.geometry(f"{CANVAS_WIDTH}x{CANVAS_WIDTH}")  # Set window size
        root.resizable(False, False)  # Disable window resize
        root.title("Boggle")  # Set window title
        self._root = root

    def run(self):
        self._root.mainloop()

    def set_message(self, message):
        self.game_screen.set_message(message)

    def display_start_screen(self):
        self._start_screen.create()

    def hide_start_screen(self):
        self._start_screen.destroy()

    def display_game_screen(self):
        self.game_screen.create()

    def hide_game_screen(self):
        self.game_screen.destroy()

    def display_end_screen(self, handle_end_screen_press):
        pass

    # def reset_tiles(self):
    #     self.game_screen.reset_tiles()
