import tkinter as tki

from boggle_board_randomizer import randomize_board
from tile_grid import TileGrid
from timer import Timer

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
BOARD_SIZE = 400
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
    def __init__(self, board, master, handle_add_coordinate):
        self._tiles_frame = None
        self._timer_frame = None
        self._timer = None
        self._master = master
        self._grid = None
        self._board = board
        self._handle_add_coordinate = handle_add_coordinate
        self._message_text = tki.StringVar()

    def create(self):
        container = tki.Frame(self._master, bg="lightblue", borderwidth=10)
        container.rowconfigure(0, weight=1)
        container.rowconfigure(1, weight=1)
        container.rowconfigure(2, weight=8)
        container.rowconfigure(3, weight=1)
        container.columnconfigure(0, weight=2)
        container.columnconfigure(1, weight=1)
        container.pack(fill=tki.BOTH, expand=True)

        message_frame = tki.Frame(container, bg="pink")
        message_frame.grid(row=0, column=0, columnspan=2, sticky=tki.NSEW)
        timer_frame = tki.Frame(container)
        timer_frame.grid(row=1, column=0, sticky=tki.NSEW)
        score_frame = tki.Frame(container, bg="cyan")
        score_frame.grid(row=1, column=1, sticky=tki.NSEW)
        tiles_frame = tki.Frame(container)
        tiles_frame.grid(row=2, column=0, sticky=tki.NSEW)
        words_frame = tki.Frame(container, bg="turquoise")
        words_frame.grid(row=2, column=1, sticky=tki.NSEW)
        message_frame = tki.Frame(container, bg="pink")
        message_frame.grid(row=3, column=0, columnspan=2, sticky=tki.NSEW)

        self._timer_frame = timer_frame
        self._tiles_frame = tiles_frame

        self._create_timer()
        self._create_grid()
        # self._create_message_label()

    def handle_time_out(self):
        pass

    def _create_timer(self):
        self._timer = Timer(self._timer_frame, "03:00", self.handle_time_out)
        self._timer.create()

    def destroy(self):
        frames = [self._top_frame, self._center_frame, self._bottom_frame]
        for frame in frames:
            if frame:
                frame.destroy()

    def _create_bottom_bar(self):
        bottom_frame = tki.Frame(self._master, bg="lightgray", height=TOP_BAR_HEIGHT)
        bottom_frame.pack(fill=tki.X, side=tki.BOTTOM)
        self._bottom_frame = bottom_frame

    def _create_center_frame(self):
        center_frame = tki.Frame(self._master, bg="lightpink")
        center_frame.columnconfigure(0, weight=2)
        center_frame.columnconfigure(1, weight=1)
        center_frame.pack(fill=tki.BOTH, expand=True)
        self._center_frame = center_frame
        left_frame = tki.Frame(center_frame, bg="blue")
        left_frame.grid(row=0, column=0)
        right_frame = tki.Frame(center_frame, bg="brown")
        left_frame.grid(row=0, column=1)
        self._left_frame = left_frame
        self.right_frame = right_frame

        # self._grid = TileGrid(right_frame, self._board, BOARD_SIZE, self._handle_add_coordinate,
        #                       self.set_message,
        #                       self.set_message)
        # self._grid.create()

    def _create_top_bar(self):
        top_frame = tki.Frame(self._master, bg="lightgray", height=BOTTOM_BAR_HEIGHT)
        top_frame.pack(fill=tki.X)
        top_frame.pack_propagate(0)
        self._top_frame = top_frame

    def _create_grid(self):
        self._grid = TileGrid(self._tiles_frame, self._board, BOARD_SIZE, self._handle_add_coordinate, self.set_message,
                              self.set_message)
        self._grid.create()

    def set_message(self, message):
        self._message_text.set(message)

    def _create_message_label(self):
        frame = tki.Frame(self._top_frame)
        frame.pack(fill=tki.X, anchor=tki.S)
        label = tki.Label(frame, textvariable=self._message_text)
        label.pack()

    def _create_message_lable(self):
        fra

    def reset_tiles(self):
        self._grid.reset_word()


class EndScreenGui:
    def __init__(self, handle_end_screen_press):
        self._handle_end_screen_press = handle_end_screen_press
