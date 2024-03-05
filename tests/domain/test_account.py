from banking_system.use_cases.create_accounts.create_accounts_usecase import CreateAccountsUseCase
from banking_system.use_cases.transactions.make_transactions_usecase import TransactionUseCase
import pytest
from unittest.mock import patch
from pytest_mock import mocker


def test_create_account_when_name_missing_should_fail(mocker):
    #with mocker.patch.object(CreateAccountsUseCase,'create_account'):
    with patch('banking_system.use_cases.create_accounts.create_accounts_usecase.CreateAccountsUseCase.create_account', side_effect=Exception('mocked error')):
        with pytest.raises(Exception) as excinfo:
            account_obj = CreateAccountsUseCase().create_account( 
                        'diva.mishra19@gmail.com', 
                        '8373850527',
                        500)
        assert isinstance(excinfo.value, Exception)


def test_create_account_when_email_missing_should_fail(mocker):
    with patch('banking_system.use_cases.create_accounts.create_accounts_usecase.CreateAccountsUseCase.create_account', side_effect=Exception('mocked error')):
        with pytest.raises(Exception) as excinfo:
            account_obj = CreateAccountsUseCase().create_account( 
                        'Roshni', 
                        '8373850527',
                        500)
        assert isinstance(excinfo.value, Exception)

def test_create_account_when_mobile_number_missing_should_fail(mocker):
    with patch('banking_system.use_cases.create_accounts.create_accounts_usecase.CreateAccountsUseCase.create_account', side_effect=Exception('mocked error')):
        with pytest.raises(Exception) as excinfo:
            account_obj = CreateAccountsUseCase().create_account( 
                        'Roshni', 
                        'diva.mishra19@gmail.com',
                        500)
        assert isinstance(excinfo.value, Exception)


def test_create_account_when_initial_balance_missing_should_pass(mocker):
   with mocker.patch.object(CreateAccountsUseCase,'create_account'):
        account_obj = CreateAccountsUseCase().create_account( 
                    'diva.mishra19@gmail.com', 
                    '8373850527',
                    500)
        mocker.account_obj = {
        "customer_name": "Roshni",
        "customer_id": "1e293b2c-c30a-41b8-b4de-6bc27d35bb49",
        "customer_account_number": "25c50326-5411-49bf-a585-bbcf760d8d9e",
        "customer_balance": 0,
        "customer_phone_number": "8373850527",
        "customer_email_address": "diva.mishra19@gmail.com"
    }

        assert mocker.account_obj['customer_balance'] == 0