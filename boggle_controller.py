from boggle_gui import BoggleGui
from boggle_model import BoggleModel


class BoggleController:
    def __init__(self):
        self._model = BoggleModel()
        self._gui = BoggleGui(self.on_start_screen_press, self._model.add_coordinate)

    def run(self):
        self._gui.display_start_screen()
        self._gui.run()

    def on_start_screen_press(self):
        self._gui.hide_start_screen()
        self._gui.display_game_screen()
