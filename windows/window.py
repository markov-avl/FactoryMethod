from abc import abstractmethod

from PySide6.QtWidgets import QWidget, QLayout

from languages import Language


class Window(QWidget):
    _x: int
    _y: int
    _width: int
    _height: int
    _layout: QLayout
    _language: Language

    @abstractmethod
    def __init__(self, language: Language = None, parent=None):
        super().__init__(parent)
        self._language = language

    @abstractmethod
    def update_language(self, language: Language) -> None:
        ...
