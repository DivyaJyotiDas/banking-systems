from banking_system.repository.base import Repo
from banking_system.repository import filerepo

class AccountRepository(filerepo.FileRepo):
    def __init__(self) -> None:
        self.repo = filerepo.get_file_db()

    def save_account(self, account_details):
        self.repo.create(account_details)

    def deposit(self, account, amount):
        account_id = account.get('customer_account_number')
        self.repo.update(account_id, 'customer_balance', amount)

    def withdraw(self, account, amount):
        account_id = account.get('customer_account_number')
        self.repo.update(account_id, 'customer_balance', -amount)

    def get_balance(self, account_id):
        return self.repo.get_balance(account_id)

    def find_account_by_id(self, account_id):
        return self.repo.list(account_id)

    def find_accounts_by_customer_id(self, customer_id):
        return self.repo.list(customer_id)