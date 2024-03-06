from banking_system.domain.customer import Customer
from banking_system.repository.account_repository import AccountRepository
from banking_system.repository.filerepo import FileRepo
import pytest, os
from unittest.mock import patch
from pytest_mock import mocker

FILE_PATH=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_file_db.json')

def test_create_when_account_details_provided_should_dump_json_in_file(mocker):
    test_account = {
        "customer_name": "Roshni",
        "customer_id": "05bb9089-eb0b-4eb0-a07f-b3f26770bc14",
        "customer_account_number": "6767b700-ac3c-4ef5-9cab-5576b7a1890d",
        "customer_balance": 500,
        "customer_phone_number": "8373850527",
        "customer_email_address": "diva.mishra19@gmail.com"
    }
    assert FileRepo(file_db=FILE_PATH).create(test_account) is None

def test_deposit_when_amount_provided_should_deposit(mocker):
    test_account = {
        "customer_name": "Roshni",
        "customer_id": "05bb9089-eb0b-4eb0-a07f-b3f26770bc14",
        "customer_account_number": "6767b700-ac3c-4ef5-9cab-5576b7a1890d",
        "customer_balance": 500,
        "customer_phone_number": "8373850527",
        "customer_email_address": "diva.mishra19@gmail.com"
    }
    assert FileRepo(file_db=FILE_PATH) \
        .update('6767b700-ac3c-4ef5-9cab-5576b7a1890d', 
                'customer_balance', 100).get('customer_balance')== test_account['customer_balance']+100
    
def test_withdrawl_when_amount_provided_should_withdraw(mocker):
    test_account = {
        "customer_name": "Roshni",
        "customer_id": "05bb9089-eb0b-4eb0-a07f-b3f26770bc14",
        "customer_account_number": "6767b700-ac3c-4ef5-9cab-5576b7a1890d",
        "customer_balance": 500,
        "customer_phone_number": "8373850527",
        "customer_email_address": "diva.mishra19@gmail.com"
    }
    assert FileRepo(file_db=FILE_PATH) \
        .update('6767b700-ac3c-4ef5-9cab-5576b7a1890d', 
                'customer_balance', -100).get('customer_balance')== 500

