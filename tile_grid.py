import tkinter as tki


class TileGrid:
    def __init__(self, master, board, board_size, click_handler):
        self._master = master
        self._board = board
        self._click_handler = click_handler
        self._board_size = board_size
        self._buttons = {}
        self._main_frame = None

    def create(self):
        main_frame = tki.Frame(master=self._master, bg='lightgreen')
        main_frame.place(width=self._board_size, height=self._board_size, x=10, y=5)
        self._main_frame = main_frame
        for i in range(4):
            main_frame.rowconfigure(i, weight=1)
            for j in range(4):
                main_frame.columnconfigure(j, weight=1)
                handler = self.create_tile_press_handler((i, j))
                button = tki.Button(self._main_frame, text=self._board[i][j])
                button.grid(row=i, column=j, sticky=tki.NSEW)
                button.bind("<Button-1>", handler)
                self._buttons[(i, j)] = button

    def create_tile_press_handler(self, coordinate):
        # Call the click handler with the board coordinates pressed
        def on_tile_press(event):
            event.widget.config(relief=tki.SUNKEN)
            self._click_handler(coordinate, event)
            return "break"
        return on_tile_press
