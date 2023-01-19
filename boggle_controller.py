from boggle_gui import BoggleGui


class BoggleController:
    def __init__(self):
        self._gui = BoggleGui(self.on_start_screen_press)

    def run(self):
        self._gui.display_start_screen()
        self._gui.run()

    def on_start_screen_press(self):
        self._gui.hide_start_screen()
        self._gui.display_game_screen()
