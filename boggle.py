import tkinter as tki
import time
from boggle_board_randomizer import randomize_board

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
BAR_HEIGHT = 50
BOARD_SIZE = 400
GAME_TIME = "03:00"


class MyApp:
    def __init__(self):
        self._board = None
        self.current_path = []

        # Create root
        root = tki.Tk()
        root.geometry(f"{CANVAS_WIDTH}x{CANVAS_WIDTH}")  # Set window size
        root.resizable(False, False)  # Disable window resize
        root.title("Boggle")  # Set window title
        self._root = root

        # Create top bar
        top_frame = tki.Frame(self._root, bg="lightgray", height=BAR_HEIGHT)
        top_frame.pack(fill=tki.X)
        self._top_frame = top_frame
        # Create bottom bar
        bottom_frame = tki.Frame(self._root, bg="lightgray", height=BAR_HEIGHT)
        bottom_frame.pack(fill=tki.X, side=tki.BOTTOM)
        self._bottom_frame = bottom_frame
        # Center frame
        center_frame = tki.Frame(self._root, bg="lightpink")
        center_frame.pack(fill=tki.BOTH, expand=True)
        self._center_frame = center_frame
        # Create timer
        lable_text_change = tki.StringVar()
        timer_label = tki.Label(self._top_frame, textvariable=lable_text_change)
        lable_text_change.set(GAME_TIME)
        timer_label.pack()
        self._timer_label = timer_label
        self._timer_text = lable_text_change
        # Create tile grid
        # self._tile_grid = MyApp.TileGrid(root)


    def _initialize_board(self):
        self._board = randomize_board()
        self._tile_grid = MyApp.TileGrid(self._center_frame, self._board)
        # TODO: Validate board?

    def run(self):
        self._initialize_board()
        self.display_countdown()
        self.bind_keys()
        self._root.mainloop()

    def display_countdown(self):
        txt = self.countdown()
        if txt is not None:
            self._timer_text.set(txt)
            self._root.after(1000, self.display_countdown)


    def countdown(self):
        time_str = self._timer_text.get()
        minute, second = int(time_str[0:2]), int(time_str[3:])
        if second == 0:
            if minute == 0:
                return
            minute -= 1
            second = 59
        else:
            second -= 1

        str_sec = '0' + str(second) if len(str(second)) == 1 else str(second)
        str_min = '0' + str(minute) if len(str(minute)) == 1 else str(minute)

        return str_min + ':' + str_sec

    def bind_keys(self):
        for coord, button in self._tile_grid.get_buttons().items():
            i, j = coord

            def _on_click(event):
                event.widget.config(relief=tki.SUNKEN)
                return "break"
            button.bind("<Button-1>", _on_click)

    class TileGrid:
        def __init__(self, master, board):
            self._master = master
            self._board = board
            self._buttons = {}
            main_frame = tki.Frame(master=self._master, bg='lightgreen')
            main_frame.place(width=BOARD_SIZE, height=BOARD_SIZE, x=10, y=5)
            self._main_frame = main_frame
            for i in range(4):
                main_frame.rowconfigure(i, weight=1)
                for j in range(4):
                    main_frame.columnconfigure(j, weight=1)
                    # button = self.create_tile(i, j, board[i][j])
                    button = tki.Button(self._main_frame, text=board[i][j])
                    button.grid(row=i, column=j, sticky=tki.NSEW)
                    self._buttons[(i, j)] = button

        def get_buttons(self):
            return self._buttons


def main():
    app = MyApp()
    app.run()


if __name__ == "__main__":
    main()
