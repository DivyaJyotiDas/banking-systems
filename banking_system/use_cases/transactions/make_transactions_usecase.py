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
        import pdb; pdb.set_trace()
        match param:
            case 'deposit':
                acc_obj  = FileRepo(self).list(self.account_id)
                FileRepo(self).update(acc_obj, 'customer_balance', amount)
            case 'withdraw':
                Account(self.account_id).withdraw()