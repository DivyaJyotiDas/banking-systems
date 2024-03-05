from banking_system.domain.customer import Customer
from banking_system.use_cases.transactions.make_transactions_usecase import TransactionUseCase
import pytest
from unittest.mock import patch
from pytest_mock import mocker


def test_customer_creation_when_params_passed_should_convert_to_dict(mocker):
    #with mocker.patch.object(CreateAccountsUseCase,'create_account'):
    with patch('banking_system.domain.customer.Customer'):
        account_obj = Customer('name', 'email', 'phone_number', 100)

    assert account_obj.name == 'name'
    assert isinstance(account_obj.account_id, str)

def test_customer_creation_when_multiple_same_id_provided_should_fail(mocker):
    with patch('banking_system.domain.customer.Customer'):
        account_obj_1 = Customer('name', 'email', 'phone_number', 100)
        account_obj_2 = Customer('name', 'email', 'phone_number', 100)

    assert account_obj_1.to_dict()['customer_id'] != account_obj_2.to_dict()['customer_id'] 