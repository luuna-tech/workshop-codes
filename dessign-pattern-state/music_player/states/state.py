from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..music_player import MusicPlayer

class State(ABC):
    def __init__(self, music_player: 'MusicPlayer') -> None:
        self.music_player = music_player

    @abstractmethod
    def click_next(self):
        pass

    @abstractmethod
    def click_previous(self):
        pass

    @abstractmethod
    def click_play(self):
        pass

    @abstractmethod
    def click_lock(self):
        pass
