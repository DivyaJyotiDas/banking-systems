from banking_system.domain.account import Account

class TransactionUseCase(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def __init__(self, account_id, amount, transaction_type) -> None:
        """_summary_

        Args:
            account_id (_type_): _description_
            amount (_type_): _description_
            transaction_type (_type_): _description_
        """
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type

    def make_transaction(self):
        """_summary_
        """
        param = self.transaction_type.lower()
        match param:
            case 'deposit':
                Account(self.account_id, ).deposit()

            case 'withdraw':
                Account(self.account_id).withdraw()