import tkinter as tki
import tkinter.font as tkif
from color_pallete import BG_COLOR, SECONDARY_TEXT_COLOR


class EndScreenGui:
    def __init__(self, handle_play_again):
        self._center_frame = None
        self._message_frame = None
        self._container = None
        self.message = "Game ended"
        self._handle_play_again = handle_play_again

    def create(self):
        container = tki.Frame(bg=BG_COLOR)
        container.pack(fill=tki.BOTH, expand=True)
        message_frame = tki.Frame(container, border=5)
        message_frame.pack()
        self._message_frame = message_frame
        center_frame = tki.Frame(container, bg=BG_COLOR)
        center_frame.rowconfigure(0, weight=2)
        center_frame.rowconfigure(1, weight=1)
        center_frame.rowconfigure(2, weight=2)
        center_frame.columnconfigure(0, weight=2)
        center_frame.columnconfigure(1, weight=1)
        center_frame.columnconfigure(2, weight=2)
        center_frame.pack(fill=tki.BOTH, expand=True)
        self._center_frame = center_frame
        buttons_frame = tki.Frame(center_frame, bg=BG_COLOR)
        buttons_frame.grid(row=1, column=1, sticky=tki.NSEW)
        self._buttons_frame = buttons_frame

        self._container = container
        self._create_message_label()
        self._create_play_again_button()
        self._create_exit_button()

    def destroy(self):
        self._container.destroy()

    def _create_message_label(self):
        label = tki.Label(self._message_frame, text=self.message,
                          font=tkif.Font(size=16), fg=SECONDARY_TEXT_COLOR)
        label.pack()

    def _create_play_again_button(self):
        button = tki.Button(self._buttons_frame, text="Play Again", width=10,
                            height=2, font=tkif.Font(size=14),
                            command=self._handle_play_again)
        button.pack(pady=15)

    def _create_exit_button(self):
        button = tki.Button(self._buttons_frame, text="Exit", command=exit, width=10,
                            height=2, font=tkif.Font(size=14))
        button.pack(pady=15)
