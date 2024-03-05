from banking_system.domain.customer import Customer
from banking_system.repository.filerepo import FileRepo
from banking_system.validators import validation
from banking_system.custom_exception import customer_exception

class CreateAccountsUseCase(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    @validation.validate_customer
    def create_account(self, name, email, phone_number, balance):
        """_summary_

        Args:
            name (str): Name of Customer.
            email (str): Email Address of customer.
            phone_number (str): Mobile Number of customer.
            balance (float): Initial Bal of customer.

        Returns:
            Account_Object: Account Object of the customer.
        """
        try:
            cust_obj = Customer(name, email, phone_number, balance)
            return cust_obj.create_account()
        except customer_exception.AccountNotCreated as ex:
            raise ex("Account Cannot be Created.")
        except Exception as ex:
            raise ex
        
