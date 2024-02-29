#imports
from banking_system.use_cases.create_accounts.create_accounts_usecase import CreateAccountsUseCase
from banking_system.use_cases.transactions.make_transactions_usecase import TransactionUseCase


# Driver Method.
if __name__ == '__main__':
    # account_obj = CreateAccountsUseCase().create_account(
    #                     'Roshni', 
    #                     'diva.mishra19@gmail.com', 
    #                     '8373850527',
    #                     500)

    transx_obj = TransactionUseCase(
                        account_id='9a03987e-c98c-4e74-b5fb-4d94803e3a66', 
                        transaction_type='deposit').make_transaction(amount=100)
    

    transx_obj = TransactionUseCase(
                        account_id='9a03987e-c98c-4e74-b5fb-4d94803e3a66', 
                        transaction_type='withdraw').make_transaction(amount=200)
    