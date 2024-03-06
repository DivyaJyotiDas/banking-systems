from banking_system.repository.base import Repo
from banking_system.repository import filerepo
from banking_system.custom_exception import customer_exception as exc

"""
This class is Adapter class for Mananging Multiple Repositories, be it 
    *** FIle Based Repository
    *** SQL Based DB
    *** NO SQL Based DB.

As we go on adding multiple drivers repo, we need to add in Initializer and call accordingly.
"""

class AccountRepository(filerepo.FileRepo):
    def __init__(self) -> None:
        # File Based Repository
        try:
            self.repo = filerepo.get_file_db()
        except exc.RepoDriverNotFoundException as ex:
            raise ex

    def save_account(self, account_details):
        try:
            self.repo.create(account_details)
        except exc.AccountNotCreated as ex:
            raise ex

    def deposit(self, account, amount):
        try:
            account_id = account.get('customer_account_number')
            self.repo.update(account_id, 'customer_balance', amount)
        except exc.AccountDepostException as ex:
            raise ex

    def withdraw(self, account, amount):
        try:
            account_id = account.get('customer_account_number')
            self.repo.update(account_id, 'customer_balance', -amount)
        except exc.AccountWithdrawlException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_balance(self, account_id):
        try:
            return self.repo.get_balance(account_id)
        except exc.AccountBalancelException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def find_account_by_id(self, account_id):
        try:
            return self.repo.list(account_id)
        except exc.AccountNotFoundException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def find_accounts_by_customer_id(self, customer_id):
        try:
            return self.repo.list(customer_id)
        except exc.AccountNotFoundForCustomerException as ex:
            raise ex
        except Exception as ex:
            raise ex