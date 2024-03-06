import uuid
import threading

from banking_system.custom_exception import customer_exception as exc
from banking_system.repository.filerepo import FileRepo
from banking_system.repository.account_repository import AccountRepository

class Account(object):
    """
        Account class 
    """
    account_lock = threading.Lock() #Basic Class Level Lock mechanism to prevent Race condition.
    def __init__(self, name: str, balance: float, account_id=None):
        """_summary_

        Args:
            name (str): _description_
            balance (float): _description_
            account_id (_type_, optional): _description_. Defaults to None.
        """
        self.account_id = str(uuid.uuid4()) if account_id is None else account_id
        self.account_name = name +'-'+self.account_id
        self.balance = balance
        self.repo = AccountRepository()

    def __repr__(self):
        return "Account(id:{0}, name:{1})".format(self.account_id, self.account_name)
    
    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            "account_id": self.account_id,
            "account_name": self.account_name,
            "account_balance": self.balance
        }

    def create_account(self):
        """ This method responsible for creating Acoount.
        """
        try:
            self.repo.save_account(self.to_dict())
        except exc.AccountNotCreated as ex:
            raise('Account Could Not Be Created.')
        except Exception as ex:
            raise ex
    
    def deposit(self, amount):
        """This method responsible for deposit of amount in account

        Args:
            amount (float): Amount
        """
        try:
            with Account.account_lock:
                self.repo.deposit(account=self.to_dict(),  amount=amount)
        except exc.AccountDepostException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def withdraw(self, amount):
        """_summary_

        Args:
            amount (_type_): _description_
        """
        try:
            with Account.account_lock:
                self.repo.withdraw(account=self.to_dict(),  amount=amount)
        except exc.AccountWithdrawlException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_balance(self):
        """_summary_
        """
        try:
            with Account.account_lock:
                self.repo.get_balance()
        except exc.AccountBalancelException as ex:
            raise ex
        except Exception as ex:
            raise ex
