import uuid

class Account(object):
    """
        Account class 
    """
    def __init__(self, name: str, balance: float, account_id=None):
        """_summary_

        Args:
            name (str): _description_
            balance (float): _description_
            account_id (_type_, optional): _description_. Defaults to None.
        """
        self.account_id = '1' #str(uuid.uuid4())
        self.account_name = name +'-'+self.account_id
        self.balance = balance

    def __repr__(self):
        return "Account(id:{0}, name:{1})".format(self.account_id, self.account_name)
    
    def deposit(self, amount):
        """_summary_

        Args:
            amount (_type_): _description_
        """
        pass

    def withdraw(self, amount):
        """_summary_

        Args:
            amount (_type_): _description_
        """
        pass

    def get_balance(self):
        """_summary_
        """
        pass
