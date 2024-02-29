import uuid
from banking_system.domain.account import Account

class Customer(Account):
    """_summary_

    Args:
        Account (_type_): _description_
    """
    def __init__(self, name: str, email: str, phone_number: int, balance: float):
        """_summary_

        Args:
            name (str): _description_
            email (str): _description_
            phone_number (int): _description_
            balance (float): _description_
        """
        super().__init__(name, balance)
        self.cutomer_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone_number = phone_number
    
    def __repr__(self):
        return "Account(id:{0}, Accountname:{1}, Customer Name:{2}) \
                ".format(self.account_id, self.account_name, self.name)
    
    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            "Customer Name": self.name,
            "Customer ID": self.cutomer_id,
            "Account Number": self.account_id,
            "Phone Number": self.phone_number,
            "Email Address": self.email
        }