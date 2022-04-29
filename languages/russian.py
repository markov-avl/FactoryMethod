from strings import WindowNameRu, SetEnglishRu, SetRussianRu, OpenAnotherWindowRu, PlaceholderTextRu, \
    AnotherWindowNameRu, AnotherWindowCloseRu
from .language import Language


class Russian(Language):
    @property
    def window_name(self) -> str:
        return str(WindowNameRu())

    @property
    def set_english(self) -> str:
        return str(SetEnglishRu())

    @property
    def set_russian(self) -> str:
        return str(SetRussianRu())

    @property
    def open_another_window(self) -> str:
        return str(OpenAnotherWindowRu())

    @property
    def placeholder_text(self) -> str:
        return str(PlaceholderTextRu())

    @property
    def another_window_name(self) -> str:
        return str(AnotherWindowNameRu())

    @property
    def another_window_close(self) -> str:
        return str(AnotherWindowCloseRu())
