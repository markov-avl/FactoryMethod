from PySide6.QtWidgets import QPushButton, QVBoxLayout

from languages import Language
from windows.window import Window


class AnotherWindow(Window):
    _x = 100
    _y = 125
    _width = 320
    _height = 180

    def __init__(self, language: Language, parent=None):
        super().__init__(language, parent)
        self._layout = QVBoxLayout()
        self._close = QPushButton()
        self._init_ui()

    def _init_ui(self) -> None:
        self.setGeometry(self._x, self._y, self._width, self._height)
        self.setFixedSize(self._width, self._height)
        self.setLayout(self._layout)
        self.update_language(self._language)
        self._close.clicked.connect(self.close)
        self._layout.addWidget(self._close)

    def update_language(self, language: Language) -> None:
        self._language = language
        self.setWindowTitle(self._language.another_window_name)
        self._close.setText(self._language.another_window_close)
