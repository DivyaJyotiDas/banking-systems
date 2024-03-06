class CustomException(Exception):
    def __init__(self, message, payload=None):
        self.message = message
        self.payload = payload 
    def __str__(self):
        return str(self.message)

class CustomerNotFound(CustomException):
    def __init__(self, message, payload=None):
        super().__init__(message, payload)
    
    
class AccountNotCreatedException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class AccountNotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class AccountNotFoundForCustomerException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class AccountDepostException(Exception):
     def __init__(self, *args: object) -> None:
        super().__init__(*args)

class AccountWithdrawlException(Exception):
     def __init__(self, *args: object) -> None:
        super().__init__(*args)

class AccountBalancelException(Exception):
     def __init__(self, *args: object) -> None:
        super().__init__(*args)