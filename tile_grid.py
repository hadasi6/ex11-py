import tkinter as tki
import tkinter.font as tkif
from color_pallete import TILE_GRID_TEXT_COLOR, TILE_GRID_BUTTON_COLOR



class TileGrid:
    def __init__(self, master, board, board_size, click_handler, finished_word_handler, message_setter):
        self._master = master
        self._board = board
        self._click_handler = click_handler
        self._board_size = board_size
        self._buttons = {}
        self._main_frame = None
        self._message_setter = message_setter

    def create(self):
        main_frame = tki.Frame(master=self._master)
        main_frame.pack(fill=tki.BOTH, expand=True)
        self._main_frame = main_frame
        for i in range(4):
            main_frame.rowconfigure(i, weight=1)
            for j in range(4):
                main_frame.columnconfigure(j, weight=1)
                handler = self.create_tile_press_handler((i, j))
                button = tki.Button(self._main_frame, text=self._board[i][j],
                                    bg=TILE_GRID_BUTTON_COLOR,
                                    fg=TILE_GRID_TEXT_COLOR,
                                    font=tkif.Font(size=24))
                button.grid(row=i, column=j, sticky=tki.NSEW)
                button.bind("<Button-1>", handler)
                self._buttons[(i, j)] = button

    def create_tile_press_handler(self, coordinate):
        # Call the click handler with the board coordinates pressed
        def on_tile_press(event):
            # if coordinate in self._pressed_coords:
            #     self.reset_word()
            # elif self._pressed_coords and not is_adjacent(self._pressed_coords[-1], coordinate):
            #     self.reset_word()
            # else:
            #     self._pressed_coords.append(coordinate)
            #     event.widget.config(relief=tki.SUNKEN)
            event.widget.config(relief=tki.SUNKEN)
            self._click_handler(coordinate)

            return "break"
        return on_tile_press

    def reset_word(self):
        for b in self._buttons.values():
            b.config(relief=tki.RAISED)
