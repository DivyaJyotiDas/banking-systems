#imports
from banking_system.use_cases.create_accounts.create_accounts_usecase import CreateAccountsUseCase
from banking_system.use_cases.transactions.make_transactions_usecase import TransactionUseCase


# Driver Method.
if __name__ == '__main__':
    account_obj = CreateAccountsUseCase().create_account(
                        'Roshni', 
                        'diva.mishra19@gmail.com', 
                        '8373850527',
                        500)

    # transx_obj = TransactionUseCase(
    #                     account_id='25c50326-5411-49bf-a585-bbcf760d8d9e', 
    #                     transaction_type='deposit').make_transaction(amount=100)
    

    # transx_obj = TransactionUseCase(
    #                     account_id='25c50326-5411-49bf-a585-bbcf760d8d9e', 
    #                     transaction_type='withdraw').make_transaction(amount=200)
    