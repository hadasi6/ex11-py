import tkinter as tki
import tkinter.font as tkif

from color_pallete import SECONDARY_TEXT_COLOR, BG_COLOR


class Timer:
    def __init__(self, master, game_time, timeout_handler):
        self._master = master
        self._timer_text = None
        self._timer_label = None
        self._game_time = game_time
        self._timeout_handler = timeout_handler
        self.frozen = False

    def create(self):
        lable_text_change = tki.StringVar()
        timer_label = tki.Label(self._master, textvariable=lable_text_change,
                                bg=BG_COLOR, fg=SECONDARY_TEXT_COLOR,
                                font=tkif.Font(size=14, weight="bold"))
        lable_text_change.set(self._game_time)
        timer_label.pack()
        self._timer_label = timer_label
        self._timer_text = lable_text_change
        self.display_countdown()

    def display_countdown(self):
        txt = self.countdown()
        if txt is not None:
            if not self.frozen:
                self._timer_text.set(txt)
            self._master.after(1000, self.display_countdown)

    def countdown(self):
        time_str = self._timer_text.get()
        minute, second = int(time_str[0:2]), int(time_str[3:])
        if second == 0:
            if minute == 0:
                self._timeout_handler()
                return
            minute -= 1
            second = 59
        else:
            second -= 1

        str_sec = '0' + str(second) if len(str(second)) == 1 else str(second)
        str_min = '0' + str(minute) if len(str(minute)) == 1 else str(minute)
        return str_min + ':' + str_sec

    def freeze(self):
        self.frozen = True

    def unfreeze(self):
        self.frozen = False
