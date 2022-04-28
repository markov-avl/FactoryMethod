from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton, QTextEdit, QVBoxLayout

from languages import Language, English, Russian

from .anotherwindow import AnotherWindow


class App(QMainWindow):
    # Настройки окна
    _x = 50
    _y = 75
    _width = 480
    _height = 320
    _layout = QVBoxLayout()
    _language: Language = None
    _another_window: AnotherWindow = None

    def __init__(self) -> None:
        super().__init__()
        self._main = QWidget()
        self._set_english = QPushButton()
        self._set_russian = QPushButton()
        self._open_another_window = QPushButton()
        self._text_input = QTextEdit()
        self._init_ui()
        self.show()

    # Главная функция настройки интерфейса
    def _init_ui(self) -> None:
        self.setGeometry(self._x, self._y, self._width, self._height)
        self.setFixedSize(self._width, self._height)
        self.setCentralWidget(self._main)
        self._set_main_layout()
        self._set_english.click()

    # Настройка главного макета
    def _set_main_layout(self) -> None:
        self._set_english.clicked.connect(lambda: self.update_language(English()))
        self._set_russian.clicked.connect(lambda: self.update_language(Russian()))
        self._open_another_window.clicked.connect(self._open_window)
        self._layout.addWidget(self._set_english)
        self._layout.addWidget(self._set_russian)
        self._layout.addWidget(self._open_another_window)
        self._layout.addWidget(self._text_input)
        self._main.setLayout(self._layout)

    # Используется для изменения языка программы
    def update_language(self, language: Language) -> None:
        self._language = language
        self.setWindowTitle(self._language.window_name)
        self._set_english.setText(self._language.set_english)
        self._set_russian.setText(self._language.set_russian)
        self._open_another_window.setText(self._language.open_another_window)
        self._text_input.setPlaceholderText(self._language.placeholder_text)
        if self._another_window:
            self._another_window.update_language(language)

    def _open_window(self) -> None:
        if self._another_window:
            if self._another_window.isVisible():
                return self._another_window.activateWindow()
            del self._another_window
        self._another_window = AnotherWindow(self._language)
        self._another_window.show()
