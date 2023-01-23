import tkinter as tki
import tkinter.font as tkif

from color_pallete import BG_COLOR, SECONDARY_TEXT_COLOR, USED_WORDS_BORDER_COLOR
from tile_grid import TileGrid
from timer import Timer

BOARD_SIZE = 400
GAME_TIME = "03:00"


class GameScreenGui:
    def __init__(self, master, board, handle_add_coordinate, handle_timeout):
        self._help = None
        self._help_image = None
        self._container = None
        self._score_frame = None
        self._buttons_frame = None
        self._words_frame = None
        self._score_text = tki.StringVar()
        self._score_text.set(self._score_to_text(0))
        self._message_frame = None
        self._tiles_frame = None
        self._timer_frame = None
        self._timer = None
        self._master = master
        self._grid = None
        self._board = board
        self._handle_add_coordinate = handle_add_coordinate
        self._handle_timeout = handle_timeout
        self._message_text = tki.StringVar()
        self._used_words_text = tki.StringVar()

    #
    # def set_board(self, board):
    #     self._board = board
    #     self._grid.set_board(self._board)

    def create(self):
        container = tki.Frame(self._master, bg=BG_COLOR, borderwidth=10)
        container.rowconfigure(0, weight=1)
        container.rowconfigure(1, weight=1)
        container.rowconfigure(2, weight=8)
        container.rowconfigure(3, weight=3)
        container.columnconfigure(0, weight=2)
        container.columnconfigure(1, weight=1)
        container.pack(fill=tki.BOTH, expand=True)

        message_frame = tki.Frame(container, bg=BG_COLOR)
        message_frame.grid(row=0, column=0, columnspan=2, sticky=tki.NSEW)
        timer_frame = tki.Frame(container, bg=BG_COLOR)
        timer_frame.grid(row=1, column=0, sticky=tki.NSEW)
        score_frame = tki.Frame(container, bg=BG_COLOR)
        score_frame.grid(row=1, column=1, sticky=tki.NSEW)
        tiles_frame = tki.Frame(container)
        tiles_frame.grid(row=2, column=0, sticky=tki.NSEW)
        words_frame = tki.Frame(container, bg=BG_COLOR, highlightthickness=5,
                                highlightbackground=USED_WORDS_BORDER_COLOR, border=3)
        words_frame.grid(row=2, column=1, sticky=tki.NSEW)
        buttons_frame = tki.Frame(container, bg=BG_COLOR)
        buttons_frame.grid(row=3, column=0, columnspan=2, sticky=tki.NSEW,
                           pady=10)

        self._container = container
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
        self._create_buttons()

    def _create_timer(self):
        self._timer = Timer(self._timer_frame, GAME_TIME, self._handle_timeout)
        self._timer.create()

    def destroy(self):
        self._container.destroy()

    def _create_grid(self):
        self._grid = TileGrid(self._tiles_frame, self._board, BOARD_SIZE, self._handle_add_coordinate,
                              self.set_message)
        self._grid.create()

    def set_message(self, message):
        self._message_text.set(message)

    def _create_message_label(self):
        label = tki.Label(self._message_frame, textvariable=self._message_text,
                          bg=BG_COLOR, fg=SECONDARY_TEXT_COLOR,
                          font=tkif.Font(weight="bold", size=12))
        label.pack()

    def _create_used_words_label(self):
        title = tki.Label(self._words_frame, text="Found Words\n",
                          bg=BG_COLOR, fg="black",
                          font=tkif.Font(weight="bold", size=16))
        title.pack(fill=tki.X)
        label = tki.Label(self._words_frame, textvariable=self._used_words_text,
                          bg=BG_COLOR, fg=SECONDARY_TEXT_COLOR,
                          font=tkif.Font(size=14))
        label.pack()

    def set_score_and_words(self, score, words):
        score_text = self._score_to_text(score)
        self._score_text.set(score_text)
        sorted_words = sorted(words)
        text = "\n".join(words)
        self._used_words_text.set(text)

    def _create_score_label(self):
        label = tki.Label(self._score_frame, textvariable=self._score_text,
                          bg=BG_COLOR, fg=SECONDARY_TEXT_COLOR,
                          font=tkif.Font(size=14, weight="bold"))
        label.pack()

    def reset_tiles(self):
        self._grid.reset_word()

    def _score_to_text(self, score):
        return f"Score:\n{score}"

    def reset_score_and_words(self):
        self._score_text = self._score_to_text(0)
        self._used_words_text = ""

    def _create_buttons(self):
        self._buttons_frame.columnconfigure(0, weight=1)
        self._buttons_frame.columnconfigure(1, weight=1)
        self._buttons_frame.columnconfigure(2, weight=1)
        self._buttons_frame.columnconfigure(3, weight=1)
        button_config = {
            "width": 12,
            "height": 2,
            "font": tkif.Font(weight="bold")
        }
        help_button = tki.Button(self._buttons_frame, text="Help", command=self.display_help, **button_config)
        help_button.grid(row=0, column=0)
        main_menu_button = tki.Button(self._buttons_frame, text="Main Menu", command=self._handle_timeout,
                                      **button_config)
        main_menu_button.grid(row=0, column=1)

    def display_help(self):
        help_image = tki.PhotoImage(file="help.png")
        self._help_image = help_image  # Fixes a bug in tkinter where the image is freed
        help_window = tki.Label(self._master, image=self._help_image)
        help_window.place(x=0, y=0, relheight=1, relwidth=1)
        help_window.bind("<Button-1>", self.hide_help)
        self._help = help_window
        self._timer.freeze()

    def hide_help(self, _):
        if self._help is not None:
            self._help.destroy()
            self._help = None
            self._timer.unfreeze()
