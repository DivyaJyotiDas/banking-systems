from banking_system.domain.account import Account
from banking_system.repository.filerepo import FileRepo

class TransactionUseCase(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def __init__(self, account_id, transaction_type) -> None:
        """_summary_

        Args:
            account_id (_type_): _description_
            amount (_type_): _description_
            transaction_type (_type_): _description_
        """
        self.account_id = account_id
        self.transaction_type = transaction_type

    def make_transaction(self, amount):
        """_summary_
        """
        param = self.transaction_type.lower()
        match param:
            case 'deposit':
                acc_obj  = FileRepo(self).list(self.account_id)
                return FileRepo(self).update(acc_obj, 'customer_balance', amount)
            case 'withdraw':
                acc_obj  = FileRepo(self).list(self.account_id)
                if acc_obj.get('customer_balance') - amount < 0:
                    raise Exception('Not Enough Fund in your Account.')
                return FileRepo(self).update(acc_obj, 'customer_balance', -amount)