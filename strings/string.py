from abc import ABC, abstractmethod


class String(ABC):
    @abstractmethod
    def __init__(self, string: str, length: int = 0):
        self._string = string
        self._length = length

    def __str__(self) -> str:
        if self._length < 1:
            return self._string
        words = self._string.split(' ')
        lines = words[: 1]
        for word in words[1:]:
            if len(lines[-1]) + 1 + len(word) <= self._length:
                lines[-1] += ' ' + word
            else:
                lines.append(word)
        return '\n'.join(lines)
