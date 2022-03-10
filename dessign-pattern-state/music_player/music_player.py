from states import State, LockedState

class MusicPlayer:
    state: State

    def __init__(self) -> None:
        self.state = LockedState(self)

    def change_state(self, state_cls: State):
        self.state = state_cls(self)

    def click_next(self):
        self.state.click_next()

    def click_previous(self):
        self.state.click_previous()

    def click_play(self):
        self.state.click_play()

    def click_lock(self):
        self.state.click_lock()

    def play_next(self):
        print('Reproduciendo la siguiente canción')

    def play_previous(self):
        print('Reproduciendo la canción anterior')

    def play_song(self):
        print('Empezando reproducción')


ipod = MusicPlayer()
print(ipod.state)

ipod.click_play()
print(ipod.state)

ipod.click_lock()
print(ipod.state)

ipod.click_play()
print(ipod.state)
