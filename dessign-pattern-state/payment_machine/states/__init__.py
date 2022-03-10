from .payment_state import PaymentState
from .paid_state import PaidState
from .canceled_state import CanceledState
from .pending_payment_state import PendingPaymentState

STATE_MAP = {
    PaidState.name: PaidState,
    CanceledState.name: CanceledState,
    PendingPaymentState.name: PendingPaymentState
}