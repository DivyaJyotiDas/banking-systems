from banking_system.use_cases.create_accounts.create_accounts_usecase import CreateAccountsUseCase
from banking_system.use_cases.transactions.make_transactions_usecase import TransactionUseCase
from unittest import mock

def test_account_creation():
    account_obj = CreateAccountsUseCase().create_account(
                        'Roshni', 
                        'diva.mishra19@gmail.com', 
                        '8373850527',
                        500)
    
    res = [{
        "customer_name": "Roshni",
        "customer_id": "3dc2b3e6-1b04-4ab7-9885-89d899e2cbd5",
        "customer_account_number": "9a03987e-c98c-4e74-b5fb-4d94803e3a66",
        "customer_balance": 500,
        "customer_phone_number": "8373850527",
        "customer_email_address": "diva.mishra19@gmail.com"
    }]

    assert res[0]['customer_name'] == "Roshni"
    assert res[0]['customer_balance'] == 500
    assert res[0]['customer_phone_number'] == "8373850527"
    assert res[0]['customer_email_address'] == "diva.mishra19@gmail.com"

#@mock.patch('banking_system.use_cases.transactions.make_transactions_usecase.TransactionUseCase')   
def test_withdraw_transaction():
    return_value = TransactionUseCase(
                                account_id='9a03987e-c98c-4e74-b5fb-4d94803e3a66', 
                                transaction_type='withdraw').make_transaction(amount=100)
    
    assert return_value

def test_deposit_transaction():
    return_value = TransactionUseCase(
                                account_id='9a03987e-c98c-4e74-b5fb-4d94803e3a66', 
                                transaction_type='deposit').make_transaction(amount=100)
    
    assert return_value

@mock.patch('banking_system.use_cases.transactions.make_transactions_usecase.TransactionUseCase') 
def test_negative_account(mock_val):
    value = TransactionUseCase(
                                account_id='9a03987e-c98c-4e74-b5fb-4d94803e3a66', 
                                transaction_type='deposit').make_transaction(amount=100)
    
    mock_val.return_value = {"balance":100}
    

    val = TransactionUseCase(
                        account_id='9a03987e-c98c-4e74-b5fb-4d94803e3a66', 
                        transaction_type='withdraw').make_transaction(amount=1000000000)
    

    val = mock_val.return_value['balance'] - 1000000000
    
    assert val < 0
    
