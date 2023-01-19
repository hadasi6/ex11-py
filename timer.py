import tkinter as tki


class Timer:
    def __init__(self, master, game_time, timeout_handler):
        self._master = master
        self._timer_text = None
        self._timer_label = None
        self._game_time = game_time
        self._timeout_handler = timeout_handler

    def create(self):
        lable_text_change = tki.StringVar()
        timer_label = tki.Label(self._master, textvariable=lable_text_change)
        lable_text_change.set(self._game_time)
        timer_label.pack()
        self._timer_label = timer_label
        self._timer_text = lable_text_change
        self.display_countdown()

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
