
class SalesOrder:
    state: str
    
    def __init__(self, state: str = None) -> None:
        self.state = state

    def save_state_to_db(self, state: str) -> None:
        self.state = state
        print (f'Saving {state} to db')