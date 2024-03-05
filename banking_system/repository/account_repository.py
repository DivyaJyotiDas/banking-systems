from banking_system.repository.base import Repo
from banking_system.repository import filerepo

class AccountRepository(filerepo.FileRepo):
    def __init__(self) -> None:
        self.repo = filerepo.get_file_db()

    def save_account(self, account_details):
        self.repo.create(account_details)

    def deposit(self):
        self.repo.update()

    def withdraw(self):
        self.repo.update()

    def get_balance(self, account_id):
        self.repo.get_balance(account_id)

    def find_account_by_id(self, account_id):
        self.repo.list(account_id)

    def find_accounts_by_customer_id(self, customer_id):
        self.repo.list(customer_id)