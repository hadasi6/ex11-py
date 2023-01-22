import tkinter as tki
from tile_grid import TileGrid
from timer import Timer

BOARD_SIZE = 400
BG_COLOR = "#cbbff9"


class GameScreenGui:
    def __init__(self, board, master, handle_add_coordinate):
        self._score_frame = None
        self._buttons_frame = None
        self._words_frame = None
        self._score_text = tki.StringVar()
        self._score_text.set("0")
        self._message_frame = None
        self._tiles_frame = None
        self._timer_frame = None
        self._timer = None
        self._master = master
        self._grid = None
        self._board = board
        self._handle_add_coordinate = handle_add_coordinate
        self._message_text = tki.StringVar()
        self._used_words_text = tki.StringVar()

    def create(self):
        container = tki.Frame(self._master, bg=BG_COLOR, borderwidth=10)
        container.rowconfigure(0, weight=1)
        container.rowconfigure(1, weight=1)
        container.rowconfigure(2, weight=8)
        container.rowconfigure(3, weight=2)
        container.columnconfigure(0, weight=2)
        container.columnconfigure(1, weight=1)
        container.pack(fill=tki.BOTH, expand=True)

        message_frame = tki.Frame(container, bg=BG_COLOR)
        message_frame.grid(row=0, column=0, columnspan=2, sticky=tki.NSEW)
        timer_frame = tki.Frame(container)
        timer_frame.grid(row=1, column=0, sticky=tki.NSEW)
        score_frame = tki.Frame(container, bg=BG_COLOR)
        score_frame.grid(row=1, column=1, sticky=tki.NSEW)
        tiles_frame = tki.Frame(container)
        tiles_frame.grid(row=2, column=0, sticky=tki.NSEW)
        words_frame = tki.Frame(container, bg=BG_COLOR)
        words_frame.grid(row=2, column=1, sticky=tki.NSEW)
        buttons_frame = tki.Frame(container, bg=BG_COLOR)
        buttons_frame.grid(row=3, column=0, columnspan=2, sticky=tki.NSEW)

        self._timer_frame = timer_frame
        self._tiles_frame = tiles_frame
        self._message_frame = message_frame
        self._words_frame = words_frame
        self._buttons_frame = buttons_frame
        self._score_frame = score_frame

        self._create_timer()
        self._create_grid()
        self._create_message_label()
        self._create_score_label()
        self._create_used_words_label()

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

    def _create_grid(self):
        self._grid = TileGrid(self._tiles_frame, self._board, BOARD_SIZE, self._handle_add_coordinate, self.set_message,
                              self.set_message)
        self._grid.create()

    def set_message(self, message):
        self._message_text.set(message)

    def _create_message_label(self):
        label = tki.Label(self._message_frame, textvariable=self._message_text)
        label.pack()

    def _create_used_words_label(self):
        label = tki.Label(self._words_frame, textvariable=self._used_words_text)
        label.pack()

    def set_score_and_word(self, score, words):
        self._score_text.set(str(score))
        text = "\n".join(words)
        self._used_words_text.set(text)

    def _create_score_label(self):
        label = tki.Label(self._score_frame, textvariable=self._score_text)
        label.pack()

    def reset_tiles(self):
        self._grid.reset_word()
