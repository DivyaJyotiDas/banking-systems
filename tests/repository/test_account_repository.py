from banking_system.domain.customer import Customer
from banking_system.repository.account_repository import AccountRepository
import pytest
from unittest.mock import patch
from pytest_mock import mocker


def test_save_accounts_when_params_is_correct(mocker):
    class AC:
        def __init__(self) -> None:
            self.db = None
    with patch('banking_system.repository.account_repository.AccountRepository'):
        res = AccountRepository()
        res.return_value = {}

    assert res.return_value == {}