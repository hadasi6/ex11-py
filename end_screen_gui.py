import tkinter as tki


class EndScreenGui:
    def __init__(self, message):
        self._message_frame = None
        self._container = None
        self._message = message

    def create(self):
        container = tki.Frame()
        container.pack()
        message_frame = tki.Frame(container)
        message_frame.pack()
        self._message_frame = message_frame
        center_frame = tki.Frame(container)
        center_frame.place(relx=0.5, rely=0.5, anchor=tki.CENTER)
        self._container = container
        self._create_message_label()

    def _create_message_label(self):
        label = tki.Label(self._message_frame)

