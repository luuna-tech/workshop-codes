from .state import State

class ReadyState(State):
    def click_next(self):
        self.music_player.play_next()

    def click_previous(self):
        self.music_player.play_previous()

    def click_lock(self):
        from . import LockedState
        self.music_player.change_state(LockedState)

    def click_play(self):
        from . import PlayingState

        self.music_player.play_song()
        self.music_player.change_state(PlayingState)
