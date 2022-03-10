from .state import State

class LockedState(State):
    def click_next(self):
        pass

    def click_previous(self):
        pass

    def click_lock(self):
        from . import ReadyState
        self.music_player.change_state(ReadyState)

    def click_play(self):
        pass