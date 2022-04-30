from abc import ABC, abstractmethod


class Language(ABC):
    @property
    @abstractmethod
    def window_name(self) -> str:
        ...

    @property
    @abstractmethod
    def set_english(self) -> str:
        ...

    @property
    @abstractmethod
    def set_russian(self) -> str:
        ...

    @property
    @abstractmethod
    def open_another_window(self) -> str:
        ...

    @property
    @abstractmethod
    def placeholder_text(self) -> str:
        ...

    @property
    @abstractmethod
    def another_window_name(self) -> str:
        ...

    @property
    @abstractmethod
    def another_window_close(self) -> str:
        ...
