from .state import State

class PlayingState(State):
    def click_next(self):
        self.music_player.play_next()

    def click_previous(self):
        self.music_player.play_previous()

    def click_lock(self):
        from . import LockedState
        self.music_player.change_state(LockedState)

    def click_play(self):
        from . import ReadyState
        self.music_player.change_state(ReadyState)
