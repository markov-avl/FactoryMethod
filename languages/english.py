from strings import WindowNameEn, SetEnglishEn, SetRussianEn, OpenAnotherWindowEn, PlaceholderTextEn, \
    AnotherWindowNameEn, AnotherWindowCloseEn
from .language import Language


class English(Language):
    @property
    def window_name(self) -> str:
        return str(WindowNameEn())

    @property
    def set_english(self) -> str:
        return str(SetEnglishEn())

    @property
    def set_russian(self) -> str:
        return str(SetRussianEn())

    @property
    def open_another_window(self) -> str:
        return str(OpenAnotherWindowEn())

    @property
    def placeholder_text(self) -> str:
        return str(PlaceholderTextEn())

    @property
    def another_window_name(self) -> str:
        return str(AnotherWindowNameEn())

    @property
    def another_window_close(self) -> str:
        return str(AnotherWindowCloseEn())