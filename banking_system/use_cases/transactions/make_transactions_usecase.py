from banking_system.domain.account import Account

class TransactionUseCase():
    def __init__(self, account_id, amount, transaction_type) -> None:
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type

    def make_transaction(self):
        param = self.transaction_type.lower()
        match param:
            case 'deposit':
                Account(self.account_id).deposit()

            case 'withdraw':
                Account(self.account_id).withdraw()