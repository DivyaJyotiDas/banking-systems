import uuid

class Account():
    def __init__(self, name: str, balance: float, account_id=None):
        self.account_id = '1' #str(uuid.uuid4())
        self.account_name = name +'-'+self.account_id
        self.balance = balance

    def __repr__(self):
        return "Account(id:{0}, name:{1})".format(self.account_id, self.account_name)
    
    def deposit(self):
        pass

    def withdraw():
        pass

    def get_balance():
        pass
