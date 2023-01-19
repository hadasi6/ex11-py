import tkinter as tki

from boggle_board_randomizer import randomize_board
from tile_grid import TileGrid
from timer import Timer

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
BAR_HEIGHT = 50
BOARD_SIZE = 400


class BoggleGui:
    def __init__(self, handle_start_screen_press):
        self._create_root()
        self._start_screen = StartScreenGui(self._root, handle_start_screen_press)
        self._game_screen = GameScreenGui(self._root)
        self._handle_start_screen_press = handle_start_screen_press

    def _create_root(self):
        root = tki.Tk()
        root.geometry(f"{CANVAS_WIDTH}x{CANVAS_WIDTH}")  # Set window size
        root.resizable(False, False)  # Disable window resize
        root.title("Boggle")  # Set window title
        self._root = root

    def run(self):
        self._root.mainloop()

    def display_start_screen(self):
        self._start_screen.create()

    def hide_start_screen(self):
        self._start_screen.destroy()

    def display_game_screen(self):
        self._game_screen.create()

    def hide_game_screen(self):
        self._game_screen.destroy()

    def display_end_screen(self, handle_end_screen_press):
        pass


class StartScreenGui:
    def __init__(self, master, handle_start_screen_press):
        self._master = master
        self._handle_start = handle_start_screen_press
        self._frame = None

    def create(self):
        frame = tki.Frame(self._master, bg='red')
        frame.pack(fill=tki.BOTH, expand=True)
        button = tki.Button(frame, command=self._handle_start, text="Kill Me", bg='yellow')
        button.pack()
        self._frame = frame
        # bottom_frame = tki.Frame(self._master, bg="lightgray", height=400)
        # bottom_frame.pack(fill=tki.X, side=tki.BOTTOM)

    def destroy(self):
        if self._frame is not None:
            self._frame.destroy()


class GameScreenGui:
    def __init__(self, master):
        self._timer = None
        self._master = master
        self._top_frame = None
        self._center_frame = None
        self._bottom_frame = None
        self._grid = None
        self._board = randomize_board()

    def create(self):
        self._create_top_bar()
        self._create_bottom_bar()
        self._create_center_frame()
        self._create_timer()
        self._create_grid()

    def handle_time_out(self):
        pass

    def _create_timer(self):
        self._timer = Timer(self._top_frame, "03:00", self.handle_time_out)
        self._timer.create()

    def destroy(self):
        frames = [self._top_frame, self._center_frame, self._bottom_frame]
        for frame in frames:
            if frame:
                frame.destroy()

    def _create_bottom_bar(self):
        bottom_frame = tki.Frame(self._master, bg="lightgray", height=BAR_HEIGHT)
        bottom_frame.pack(fill=tki.X, side=tki.BOTTOM)
        self._bottom_frame = bottom_frame

    def _create_center_frame(self):
        center_frame = tki.Frame(self._master, bg="lightpink")
        center_frame.pack(fill=tki.BOTH, expand=True)
        self._center_frame = center_frame

    def _create_top_bar(self):
        top_frame = tki.Frame(self._master, bg="lightgray", height=BAR_HEIGHT)
        top_frame.pack(fill=tki.X)
        self._top_frame = top_frame

    def _handle_click(self, coordinate, event):
        pass

    def _create_grid(self):
        self._grid = TileGrid(self._center_frame, self._board, 400, self._handle_click)
        self._grid.create()


class EndScreenGui:
    def __init__(self, handle_end_screen_press):
        self._handle_end_screen_press = handle_end_screen_press
