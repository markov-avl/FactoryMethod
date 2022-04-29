from abc import ABC, abstractmethod


class Language(ABC):
    _SET_RUSSIAN: str
    _OPEN_ANOTHER_WINDOW: str
    _PLACEHOLDER_TEXT: str
    _ANOTHER_WINDOW_NAME: str
    _ANOTHER_WINDOW_CLOSE: str

    @property
    @abstractmethod
    def window_name(self) -> str:
        ...

    @property
    @abstractmethod
    def set_english(self) -> str:
        ...

    @property
    def set_russian(self) -> str:
        return self._SET_RUSSIAN

    @property
    def open_another_window(self) -> str:
        return self._OPEN_ANOTHER_WINDOW

    @property
    def placeholder_text(self) -> str:
        return self._PLACEHOLDER_TEXT

    @property
    def another_window_name(self) -> str:
        return self._ANOTHER_WINDOW_NAME

    @property
    def another_window_close(self) -> str:
        return self._ANOTHER_WINDOW_CLOSE
