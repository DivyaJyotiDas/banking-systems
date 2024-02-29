#imports
from banking_system.use_cases.create_accounts.create_accounts_usecase import CreateAccountsUseCase
from banking_system.use_cases.transactions.make_transactions_usecase import TransactionUseCase


# Driver Method.
if __name__ == '__main__':
    account_obj = CreateAccountsUseCase().create_account(
                        'Divya', 
                        'divyajyotidas15@gmail.com', 
                        '8329140439',
                        1000)
    print(account_obj.to_dict())

    transx_obj = TransactionUseCase(account_id=1, amount=100, transaction_type='deposit').make_transaction()
    