import tkinter as tki

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600


class BoggleGui:
    def __init__(self, handle_start_screen_press):
        self._create_root()
        self._start_screen = None
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
        self._start_screen = StartScreenGui(self._root, self._handle_start_screen_press)

    def hide_start_screen(self):
        self._start_screen.destroy()

    def display_game_screen(self):
        pass

    def display_end_screen(self, handle_end_screen_press):
        self._handle_end_screen_press = handle_end_screen_press



class StartScreenGui:
    def __init__(self, master, handle_start_screen_press):
        self._master = master
        self._handle_start = handle_start_screen_press

        self._create()

    def _create(self):
        frame = tki.Frame(self._master, bg='red')
        frame.pack(fill=tki.BOTH, expand=True)
        button = tki.Button(frame, command=self._handle_start, text="Kill Me", bg='yellow')
        button.pack()
        self._frame = frame
        # bottom_frame = tki.Frame(self._master, bg="lightgray", height=400)
        # bottom_frame.pack(fill=tki.X, side=tki.BOTTOM)

    def destroy(self):
        self._frame.destroy()


class EndScreenGui:
    def __init__(self, handle_end_screen_press):
        self._handle_end_screen_press = handle_end_screen_press
