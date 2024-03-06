from banking_system.domain.account import Account
from banking_system.domain.customer import Customer
from banking_system.repository.filerepo import FileRepo
from banking_system.custom_exception import customer_exception as exc

class TransactionUseCase(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def __init__(self, account_id, transaction_type) -> None:
        """This method is used to initialize Transaction class.
        Args:
            account_id (str): Account Id.
            amount (float): Amount 
            transaction_type (str): set of {'deposit', 'withdraw'}
        """
        self.account_id = account_id
        self.transaction_type = transaction_type

    def make_transaction(self, amount):
        """Method responsible to interact external world(API, CLI) for deposit or withdraw
        """
        try:
            if self.transaction_type:
                param = self.transaction_type.lower()
            match param:
                case 'deposit':
                    account_obj = Customer.get_account(self.account_id)
                    return account_obj.deposit(amount)
                
                case 'withdraw':
                    account_obj = Customer.get_account(self.account_id)
                    return account_obj.withdraw(amount)
        except exc.TransactionError as ex:
            raise ex
        except Exception as ex:
            raise ex