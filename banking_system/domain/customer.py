import uuid
from banking_system.domain.account import Account

class Customer(Account):
    def __init__(self, name: str, email: str, phone_number: int, balance: float):
        super().__init__(name, balance)
        self.cutomer_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone_number = phone_number
    
    def __repr__(self):
        return "Account(id:{0}, Accountname:{1}, Customer Name:{2}) \
                ".format(self.account_id, self.account_name, self.name)
    
    def to_dict(self):
        return {
            "Customer Name": self.name,
            "Customer ID": self.cutomer_id,
            "Account Number": self.account_id,
            "Phone Number": self.phone_number,
            "Email Address": self.email
        }