import tkinter as tki
import time
from boggle_board_randomizer import randomize_board

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
BAR_HEIGHT = 50
BOARD_SIZE = 400
GAME_TIME = (0, 3) # seconds, mins, hrs


class MyApp:
    def __init__(self):
        self._board = None

        # Create root
        root = tki.Tk()
        root.geometry(f"{CANVAS_WIDTH}x{CANVAS_WIDTH}") # Set window size
        root.resizable(False, False) # Disable window resize
        root.title("Boggle") # Set window title
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

        # Create tile grid

        # Create timer
        timer_text = self.display_countdown(GAME_TIME)
        timer = tki.Label(self._top_frame, text=timer_text)
        timer.pack()
        self._timer = timer


    def display_countdown(self, time):
        return "00:00"


    def _initialize_board(self):
        self._board = randomize_board()
        self._tile_grid = MyApp.TileGrid(self._center_frame, self._board)
        # TODO: Validate board?

    def run(self):
        self._initialize_board()
        self._root.mainloop()

    class TileGrid:
        def __init__(self, master, board):
            self._master = master
            main_frame = tki.Frame(master=self._master, bg='lightgreen', width=BOARD_SIZE, height=BOARD_SIZE)
            main_frame.pack()
            self._main_frame = main_frame
            for i in range(4):
                for j in range(4):
                    label = tki.Label(self._main_frame, text=board[i][j])
                    label.grid(row=i, column=j)





def main():
    app = MyApp()
    app.run()


if __name__ == "__main__":
    main()
