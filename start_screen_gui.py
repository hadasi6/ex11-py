import tkinter as tki


class StartScreenGui:
    def __init__(self, master, handle_start_screen_press):
        self._master = master
        self._handle_start = handle_start_screen_press
        self._frame = None

    def create(self):
        frame = tki.Frame(self._master, bg='red')
        frame.pack(fill=tki.BOTH, expand=True)
        button = tki.Button(frame, command=self._handle_start, text="Kill Me", bg='yellow')
        button.place(relx=0.5, rely=0.5, anchor=tki.CENTER)
        self._frame = frame
        # bottom_frame = tki.Frame(self._master, bg="lightgray", height=400)
        # bottom_frame.pack(fill=tki.X, side=tki.BOTTOM)

    def destroy(self):
        if self._frame is not None:
            self._frame.destroy()
