from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..sales_order_business import SalesOrderBusiness

class PaymentState(ABC):
    name: str = None

    def __init__(self, sales_order_business: 'SalesOrderBusiness') -> None:
        self.sales_order_business = sales_order_business

    @abstractmethod
    def exec_side_effects(self):
        pass

    @abstractmethod
    def validate_payment(self):
        pass

    @abstractmethod
    def cancel_payment(self):
        pass
