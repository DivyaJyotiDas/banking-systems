from banking_system.domain.customer import Customer
from banking_system.repository.filerepo import FileRepo

class CreateAccountsUseCase(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def create_account(self, name, email, phone_number, balance):
        """_summary_

        Args:
            name (_type_): _description_
            email (_type_): _description_
            phone_number (_type_): _description_
            balance (_type_): _description_

        Returns:
            _type_: _description_
        """
        cust_obj = Customer(name, email, phone_number, balance)
        FileRepo(cust_obj).create()
