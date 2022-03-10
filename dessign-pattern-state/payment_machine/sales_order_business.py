from states import PaymentState, PendingPaymentState, STATE_MAP
from sales_order import SalesOrder

class SalesOrderBusiness:
    state: PaymentState

    def __init__(self, sales_order: SalesOrder) -> None:
        self.sales_order: SalesOrder = sales_order # Clase de ERPNext
        current_state = SalesOrderBusiness.get_current_state_from_sales_order(sales_order)

        self.state: PaymentState = None if not current_state else current_state(self)

    @staticmethod
    def get_current_state_from_sales_order(sales_order: SalesOrder) -> PaymentState:
        payment_state = sales_order.state

        if not payment_state:
            return

        return STATE_MAP[payment_state]

    @classmethod
    def from_new_sales_order(cls, sales_order: SalesOrder):
        sales_order_business = cls(sales_order)

        sales_order_business.change_state(PendingPaymentState)
        return sales_order_business

    def change_state(self, state_cls: PaymentState):
        self.state: PaymentState = state_cls(self)
        self.state.exec_side_effects()

        self.sales_order.save_state_to_db(self.state.name)

    def validate_payment(self):
        self.state.validate_payment()

    def cancel_payment(self):
        self.state.cancel_payment()







sales_order = SalesOrder()
business = SalesOrderBusiness.from_new_sales_order(sales_order)

sales_order = SalesOrder('Pending Payment')
business = SalesOrderBusiness(sales_order)
print(business.state)

business.validate_payment()
business.cancel_payment()
