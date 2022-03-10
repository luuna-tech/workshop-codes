from .payment_state import PaymentState
import utils as utils
from decorators import invalid_action

class CanceledState(PaymentState):
    name = 'Canceled'

    def exec_side_effects(self):
        utils.send_transactional_email()

    @invalid_action(Exception)
    def validate_payment(self):
        pass

    @invalid_action(Exception)
    def cancel_payment(self):
        pass
