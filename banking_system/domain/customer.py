import uuid
from banking_system.domain.account import Account
from banking_system.repository.account_repository import AccountRepository

class Customer(Account):
    """_summary_

    Args:
        Account (_type_): _description_
    """
    def __init__(self, name: str, email: str, phone_number: int, balance: float, customer_id=None, account_id=None):
        """_summary_

        Args:
            name (str): _description_
            email (str): _description_
            phone_number (int): _description_
            balance (float): _description_
        """
        super().__init__(name, balance, account_id=account_id)
        self.cutomer_id = str(uuid.uuid4()) if customer_id is None else customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    @classmethod
    def get_account(cls, account_id):
        account_val = AccountRepository().find_account_by_id(account_id=account_id)
        return Customer(
            customer_id=account_val['customer_id'],
            account_id=account_val['customer_account_number'],
            name=account_val['customer_name'],
            email=account_val['customer_email_address'],
            phone_number=account_val['customer_phone_number'],
            balance=account_val['customer_balance']
            )
    
    def __repr__(self):
        return "Account(id:{0}, Accountname:{1}, Customer Name:{2}) \
                ".format(self.account_id, self.account_name, self.name)
    
    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            "customer_name": self.name,
            "customer_id": self.cutomer_id,
            "customer_account_number": self.account_id,
            "customer_balance": self.balance,
            "customer_phone_number": self.phone_number,
            "customer_email_address": self.email
        }