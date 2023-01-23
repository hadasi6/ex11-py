import tkinter as tki
import tkinter.font as tkif
from color_pallete import BG_COLOR, HIGHLIGHT_COLOR


class StartScreenGui:
    def __init__(self, master, handle_start_screen_press):
        self._master = master
        self._handle_start = handle_start_screen_press
        self._frame = None

    def create(self):
        frame = tki.Frame(self._master)
        frame.pack(fill=tki.BOTH, expand=True)
        self._frame = frame
        bg_image = tki.PhotoImage(file="background.png")
        self._bg_image = bg_image  # Fixes a bug in tkinter where the image is freed
        background = tki.Label(self._frame, image=bg_image)
        background.place(x=0, y=0, relheight=1, relwidth=1)

        button = tki.Button(frame, command=self._handle_start,
                            text="Start Game", bg=HIGHLIGHT_COLOR,
                            font=tkif.Font(size=14))
        button.place(relx=0.5, rely=0.5, anchor=tki.CENTER, width=150,
                     height=75)

    def destroy(self):
        if self._frame is not None:
            self._frame.destroy()
