from .payment_state import PaymentState

class PendingPaymentState(PaymentState):
    name = 'Pending Payment'

    def exec_side_effects(self):
        pass

    def validate_payment(self):
        from .paid_state import PaidState
        self.sales_order_business.change_state(PaidState)

    def cancel_payment(self):
        from .canceled_state import CanceledState
        self.sales_order_business.change_state(CanceledState)
