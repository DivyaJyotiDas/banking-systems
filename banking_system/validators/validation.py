
def validate_customer(func):
    def inner(*args, **kwargs):
        """ Validation of Inputs can be done here.
            Leaving as of now.
        """
        #
        # Befor calling function validation.
        #
        func(*args, **kwargs)
        #
        # After calling function validation
        #
    return inner