from banking_system.domain.customer import Customer

class CreateAccountsUseCase:

    def create_account(self, name, email, phone_number, balance):
        return Customer(name, email, phone_number, balance)